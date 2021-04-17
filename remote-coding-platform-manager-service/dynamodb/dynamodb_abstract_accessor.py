import abc
import boto3

from typing import List
from dynamodb.dynamodb_accessor_int import DynamoDBAccessorInterface
from botocore.exceptions import ClientError


class AbstractDynamoDBAccessor(DynamoDBAccessorInterface):
    "Abtract class implementing DynamoDbAccessor interface"

    def __init__(self, table_name: str) -> None:
        super().__init__()
        self._table_name = table_name
        self._dynamodb = boto3.resource(
            'dynamodb', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")
        self._table = self._dynamodb.Table(table_name)

    def get_all_items(self) -> List[any]:
        items = []
        try:
            response = self._dynamodb.scan()
        except ClientError as err:
            raise err

        print(f"Got response: {response}")
        for item in response["Items"]:
            deserialized = self.deserialize(item)
            items.append(deserialized)
        return items

    @abc.abstractclassmethod
    def deserialize(self, item) -> any:
        """
        Function which deserialize an item from the databse
        @param item - Item to be deserialized
        @return: List of all items in the dynamodb table
        """
        raise NotImplementedError

import abc

from typing import List, Optional, Union
from dynamodb.dynamodb_accessor_int import DynamoDBAccessorInterface
from botocore.exceptions import ClientError
from boto3 import dynamodb


class AbstractDynamoDBAccessor(DynamoDBAccessorInterface):
    "Abtract class implementing DynamoDbAccessor interface"

    def __init__(self, dynamo_db_client: dynamodb, table_name: str, partition_key_name: str, sort_key_name: Optional[str] = None) -> None:
        super().__init__()
        self._table_name = table_name
        self._dynamodb = dynamo_db_client
        self._table = self._dynamodb.Table(table_name)
        self.__partition_key_name = partition_key_name
        self.__sort_key_name = sort_key_name

    def get_all_items(self) -> List[any]:
        items = []
        try:
            response = self._table.scan()
        except ClientError as err:
            raise err

        print(f"Got response: {response}")
        for item in response["Items"]:
            deserialized = self.deserialize(item)
            items.append(deserialized)
        return items

    def get_item(self, partition_key: Union[str, int], sort_key: Optional[Union[str, int]] = None) -> Optional[any]:
        key = {self.__partition_key_name: partition_key}
        if self.__sort_key_name and sort_key is not None:
            key[self.__sort_key_name] = sort_key

        try:
            response = self._table.get_item(Key=key)
        except ClientError as err:
            raise err

        return self.deserialize(response['Item'])

    @abc.abstractclassmethod
    def deserialize(self, item) -> any:
        """
        Function which deserialize an item from the databse
        @param item - Item to be deserialized
        @return: List of all items in the dynamodb table
        """
        raise NotImplementedError

import boto3

from typing import List, Type, TypeVar
from dynamodb.dynamodb_accessor_int import DynamoDBAccessorInterface
from boto3.dynamodb.types import TypeDeserializer
from botocore.exceptions import ClientError
from marshmallow import EXCLUDE

_U = TypeVar("_U")
deserializer = TypeDeserializer()


class AbstractDynamoDBAccessor(DynamoDBAccessorInterface):
    "Abtract class implementing DynamoDbAccessor interface"

    def __init__(self, table_name: str, model_object: Type[_U]) -> None:
        super().__init__()
        self._table_name = table_name
        self._Model = model_object
        self._dynamodb = boto3.resource(
            'dynamodb', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")
        self._table = self._dynamodb.Table(table_name)

    def get_all_items(self) -> List[any]:
        items = []
        try:
            response = self._dynamodb.scan()
        except ClientError as err:
            raise err
        else:
            for item in response["Items"]:
                deserialized = {
                    k: deserializer.deserialize(v) for k, v in item}
                items.append(self._Model.Schema().load(
                    deserialized, unknown=EXCLUDE))
        return items

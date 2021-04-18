
from tests.configs.conftest_dynamodb import mock_boto_resource_client
from unittest.mock import patch

from dynamodb.dynamodb_question_accessor import AbstractDynamoDBAccessor


def test_WHEN_ddb_get_all_items_THEN_question_ddb_accessor_deserialize_correctly(
        mocker,
        questions_dynamodb_accessor_instance,
        valid_question_json,
        mock_boto_resource_client):

    mocker.patch(
        "dynamodb.dynamodb_question_accessor.boto3.resource",
        mock_boto_resource_client
    )

    result = questions_dynamodb_accessor_instance.get_all_items()

    print(result)

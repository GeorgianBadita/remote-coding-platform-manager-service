from typing import Dict
from dynamodb.dynamodb_question_accessor import QuestionDynamoDBAccessor
import pytest


@pytest.fixture
def questions_dynamodb_accessor_instance() -> QuestionDynamoDBAccessor:
    return QuestionDynamoDBAccessor("QUESTION", partition_key_name="question_id")


@pytest.fixture
def valid_question_json() -> Dict[any, any]:
    return {
        "difficulty": "EASY",
        "hints": [

        ],
        "input_signature": [
            "ARRAY",
            "NUMBER"
        ],
        "optimal_complexity": "O(n)",
        "output_signature": [
            "ARRAY"
        ],
        "question_id": "2a1e06b9-cd6e-4a2b-aee4-7cb0bcdfd61b",
        "question_name": "TwoSum",
        "statement": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.",
        "supported_languages": [
            "python"
        ],
        "tags": [
            "Array",
            "HashTable"
        ],
        "test_cases": [
            [
                {
                    "type": "ARRAY",
                    "value": [
                        3,
                        5,
                        -4,
                        8,
                        11,
                        1,
                        -1,
                        6
                    ]
                },
                {
                    "type": "NUMBER",
                    "value": 10
                }
            ],
            [
                {
                    "type": "ARRAY",
                    "value": [
                        4,
                        6,
                        -1,
                        3
                    ]
                },
                {
                    "type": "NUMBER",
                    "value": 4
                }
            ]
        ],
        "urls_to_official_solutions": {
            "python": [
                "s3://code-test-bucket-8efc083c-ca7f-43fc-b059-8035ad2b6bbf/questions/easy/TwoSum/python/solutions/twoSumOfficialSolution_1.py"
            ]
        },
        "urls_to_test_code": {
            "python": "s3://code-test-bucket-8efc083c-ca7f-43fc-b059-8035ad2b6bbf/questions/easy/TwoSum/python/twoSumTests.py"
        }
    }


class TableMock:
    def scan():
        return {
            "Items": valid_question_json()
        }


class BotoResourceClient:
    def Table(self, name):
        return TableMock()


@pytest.fixture
def mock_boto_resource_client() -> callable:
    def resource(*args, **kwargs):
        print("I AM CALLED")
        return BotoResourceClient()

    return resource

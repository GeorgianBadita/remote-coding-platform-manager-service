from dynamodb.dynamodb_abstract_accessor import AbstractDynamoDBAccessor
from marshmallow_dataclass import dataclass as marshmallow_dataclass


@marshmallow_dataclass
class Question:
    question_id: str
    question_name: str
    statement: str
    hints: list
    optimal_complexity: str
    tags: list
    difficulty: str
    test_cases: map
    input_signature: list
    output_signature: list
    supported_languages: list
    urls_to_official_solution: map
    urls_to_test_code: map


QuestionsDynamoDBAccessor = AbstractDynamoDBAccessor("QUESTIONS", Question)

import boto3
from model.programming_languages import ProgrammingLanguages
from typing import Dict, List, Optional
from model.test_case import TestCase, TestCaseArg
from model.data_type import DataType
from model.question import Question, QuestionDifficulty
from dynamodb.dynamodb_abstract_accessor import AbstractDynamoDBAccessor


class QuestionDynamoDBAccessor(AbstractDynamoDBAccessor):

    def __init__(self, table_name: str, partition_key_name: str, sort_key_name: Optional[str] = None):
        ddb_client = boto3.resource(
            'dynamodb', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")
        super().__init__(ddb_client, table_name, partition_key_name, sort_key_name)

    def deserialize(self, item) -> any:
        question_id = item['question_id']
        question_name = item['question_name']
        difficulty = QuestionDifficulty.return_enum_value_or_throw(
            item['difficulty'])
        statement = item['statement']
        tags = item['tags']
        hints = item['hints']
        optimal_complexity = item['optimal_complexity']
        input_signature = [DataType.return_enum_value_or_throw(
            value) for value in item['input_signature']]
        output_signature = [DataType.return_enum_value_or_throw(
            value) for value in item['output_signature']]
        supported_languages = [ProgrammingLanguages.return_enum_value_or_throw(
            value) for value in item['supported_languages']]
        test_cases = self.__deserialize_test_cases(item['test_cases'])
        urls_to_official_solutions = self.__deserialize_urls(
            item['urls_to_official_solutions'])
        urls_to_test_code = self.__deserialize_urls(item['urls_to_test_code'])

        return Question(
            question_id=question_id,
            question_name=question_name,
            statement=statement,
            hints=hints,
            optimal_complexity=optimal_complexity,
            tags=tags,
            difficulty=difficulty,
            test_cases=test_cases,
            input_signature=input_signature,
            output_signature=output_signature,
            supported_languages=supported_languages,
            urls_to_official_solution=urls_to_official_solutions,
            urls_to_test_code=urls_to_test_code
        )

    def __deserialize_test_cases(self, test_cases: any) -> List[TestCase]:
        deserialized_test_cases: List[TestCase] = [
            self.__deserialize_test_case(test_case) for test_case in test_cases]
        return deserialized_test_cases

    def __deserialize_test_case(self, test_case: List[any]) -> TestCase:
        args: List[TestCaseArg] = []
        for arg in test_case:
            arg_type = DataType.return_enum_value_or_throw(arg['type'])
            arg_value = arg['value']
            if self.__valid_arg_type_value(arg_type, arg_value):
                args.append(TestCaseArg(arg_type, arg_value))
            else:
                raise ValueError(
                    f"Value: {arg_value} is not of type: {arg_type}")

    def __valid_arg_type_value(self, arg_type: DataType, arg_value: any) -> bool:
        #TODO: implementation
        return True

    def __deserialize_urls(self, urls: any) -> Dict[ProgrammingLanguages, List[str]]:
        result: Dict[ProgrammingLanguages, List[str]] = {}

        for supported_language in urls:
            language = ProgrammingLanguages.return_enum_value_or_throw(
                supported_language)
            urls_for_language = urls[supported_language]
            result[language] = urls_for_language
        return result


QuestionDDBAccessor = QuestionDynamoDBAccessor(
    "QUESTIONS", partition_key_name="question_id")

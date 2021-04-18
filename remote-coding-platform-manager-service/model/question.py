from model.generic_enum import GenericEnum
from model.generic_data_class import GenericDataClass
from typing import List, Dict
from enum import Enum
from dataclasses import dataclass

from model.test_case import TestCase
from model.programming_languages import ProgrammingLanguages
from model.data_type import DataType


class QuestionDifficulty(GenericEnum, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"

    def return_enum_value_or_throw(value_to_find):
        for enum_value in QuestionDifficulty:
            if value_to_find == enum_value.value:
                return enum_value
        raise ValueError(
            f"{value_to_find} does not exist in QuestionDifficulty enum")


@dataclass
class Question(GenericDataClass):
    question_id: str
    question_name: str
    statement: str
    hints: List[str]
    optimal_complexity: str
    tags: List[str]
    difficulty: QuestionDifficulty
    test_cases: List[TestCase]
    input_signature: List[DataType]
    output_signature: List[DataType]
    supported_languages: List[ProgrammingLanguages]
    urls_to_official_solution: Dict[ProgrammingLanguages, List[str]]
    urls_to_test_code: Dict[ProgrammingLanguages, List[str]]

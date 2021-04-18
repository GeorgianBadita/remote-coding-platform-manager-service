from enum import Enum
from model.generic_enum import GenericEnum


class ProgrammingLanguages(GenericEnum, Enum):
    PYTHON = "python"
    CPP = "cpp"

    def return_enum_value_or_throw(value_to_find):
        for enum_value in ProgrammingLanguages:
            if value_to_find == enum_value.value:
                return enum_value
        raise ValueError(
            f"{value_to_find} does not exist in ProgrammingLanguages enum")

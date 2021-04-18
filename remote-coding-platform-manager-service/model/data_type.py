from enum import Enum
from model.generic_enum import GenericEnum


class DataType(GenericEnum, Enum):
    ARRAY = "ARRAY"
    NUMBER = "NUMBER"

    def return_enum_value_or_throw(value_to_find):
        for enum_value in DataType:
            if value_to_find == enum_value.value:
                return enum_value
        raise ValueError(f"{value_to_find} does not exist in DataType enum")

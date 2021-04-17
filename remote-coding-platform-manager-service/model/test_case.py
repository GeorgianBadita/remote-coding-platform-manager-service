from model.data_type import DataType
from typing import List


class TestCaseArg:
    def __init__(self, arg_type: DataType, value: any) -> None:
        self.__type = arg_type
        self.__value = value

    @property
    def arg_type(self) -> DataType:
        return self.__type

    @arg_type.setter
    def arg_type(self, new_arg_type: DataType) -> None:
        self.__type = new_arg_type

    @property
    def value(self) -> any:
        return self.__value

    @value.setter
    def value(self, new_value: any) -> None:
        self.__value = new_value


class TestCase:

    def __init__(self, args: List[TestCaseArg]) -> None:
        self.__args = args

    @property
    def test_case_args(self) -> List[TestCaseArg]:
        return self.__args

    @test_case_args.setter
    def test_case_args(self, new_test_case_args: List[TestCaseArg]) -> None:
        self.__args = new_test_case_args

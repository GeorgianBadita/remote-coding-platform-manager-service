from pynamodb.models import Model
from pynamodb.attributes import JSONAttribute, UnicodeAttribute, ListAttribute


class QuestionModel(Model):
    """
    A DynamoDB Question
    """

    class Meta:
        table_name = "QUESTIONS"

    question_id = UnicodeAttribute(attr_name="question_id", hash_key=True)
    question_name = UnicodeAttribute(attr_name="question_name", range_key=True)

    statement = UnicodeAttribute(attr_name="statement", null=False)
    hints = ListAttribute(attr_name="hints", of=UnicodeAttribute)
    optimal_complexity = UnicodeAttribute(
        attr_name="optimal_complexity", null=False)
    tags = ListAttribute(attr_name="tags", of=UnicodeAttribute)
    test_cases = JSONAttribute(attr_name="test_cases", null=False)
    input_signature = ListAttribute(
        attr_name="input_signature", of=UnicodeAttribute)
    output_signature = ListAttribute(
        attr_name="output_signature", of=UnicodeAttribute)

    difficulty = UnicodeAttribute(null=False)
    supported_languages = ListAttribute(
        attr_name="supported_languages", of=UnicodeAttribute)
    urls_to_official_solutions = JSONAttribute(
        attr_name="urls_to_official_solutions", null=False)
    urls_to_test_code = JSONAttribute(
        attr_name="urls_to_test_code", null=False)

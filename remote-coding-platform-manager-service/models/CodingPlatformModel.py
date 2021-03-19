from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute


class CodingPlatformModel(Model):
    """
    Model for CodingPlatform Items
    """

    class Meta:
        table_name = "CODING_PLATFORM"

    user_email = UnicodeAttribute(attr_name="user_email", hash_key=True)
    source = UnicodeAttribute(attr_name="source", range_key=True)

    username = UnicodeAttribute(attr_name="username")
    url_to_profile_picture = UnicodeAttribute(
        attr_name="url_to_profile_picture")
    sumbissions = ListAttribute(attr_name="submissions", of=UnicodeAttribute)
    solved_questions = ListAttribute(
        attr_name="solved_questions", of=UnicodeAttribute)
    tried_questions = ListAttribute(
        attr_name="tried_questions", of=UnicodeAttribute)

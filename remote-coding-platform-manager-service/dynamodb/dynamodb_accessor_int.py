import abc
from typing import List, Optional, Union


class DynamoDBAccessorInterface:

    @abc.abstractclassmethod
    def get_all_items(self) -> List[any]:
        """
        Function which retrieves all items from the database
        @return: List of all items in the dynamodb table
        @raise: ClientError if items retrieval fails
        """
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_item(self, partition_key: Union[str, int], sort_key: Optional[Union[str, int]]) -> Optional[any]:
        """
        Function for retrieving one item from the dynamodb table
        @param: partition_key - partition key value of the item
        @param: sort_key
        @return: Item if any item matches the given conditions, None otherwise
        @raise: ClientError if item retrieval fails
        """
        raise NotImplementedError

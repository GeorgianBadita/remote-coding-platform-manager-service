import json
from enum import Enum


class EnumEncoder(json.JSONEncoder):
    def default(self, o: any) -> any:
        if isinstance(o, Enum):
            return o.name
        return json.JSONEncoder.default(self, o)


class GenericEnum:
    def to_json(self) -> str:
        return json.dumps(self.__dict__, cls=EnumEncoder, indent=1, sort_keys=True)

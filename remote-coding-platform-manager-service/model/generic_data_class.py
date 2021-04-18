import json
from dataclasses import dataclass, asdict


@dataclass
class GenericDataClass:
    def to_json(self) -> str:
        return json.dumps(asdict(self))

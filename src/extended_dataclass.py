from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DataClassPlus:
    def from_dict(self, dct: Dict):
        for k, v in dct.items():
            target_type = self.__annotations__[k]
            if target_type in {list, List}:
                # TODO: handle iterables
                print(str(v) + " is list")
            # elif isinstance(target_type, _GenericAlias) and target_type.__args__:  # this is for list
            #     for arg in target_type.__args__:
            #         pass
            elif issubclass(target_type, DataClassPlus):
                v = target_type().from_dict(v)
            setattr(self, k, v)
        return self

    def to_dict(self):
        dct = dict()
        for k, v in self.__dict__.items():
            if isinstance(v, DataClassPlus):
                dct[k] = v.to_dict()
                continue
            dct[k] = v
        return dct

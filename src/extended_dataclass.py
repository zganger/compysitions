from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Dict, Iterable


class EnumEncodingSetting(IntEnum):
    VALUE = 0
    NAME = 1


class EncodingSettingException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


@dataclass
class DataClassPlus:
    def from_dict(self, dct: Dict):
        for k, v in dct.items():
            target_type = self.__annotations__[k]
            if hasattr(target_type, "__origin__"):
                target_subtype = target_type.__origin__
                if issubclass(target_subtype, Iterable):
                    # assuming only one arg for now - this could have many?
                    target_member_type = target_type.__args__[0]
                    vals = v
                    if issubclass(target_member_type, DataClassPlus):
                        vals = [target_member_type().from_dict(val) for val in vals]
                    v = target_subtype(vals)
            elif issubclass(target_type, DataClassPlus):
                v = target_type().from_dict(v)
            elif issubclass(target_type, Enum):
                if self._enum_encoding_setting() == EnumEncodingSetting.VALUE:
                    v = target_type(v)
                elif self._enum_encoding_setting() == EnumEncodingSetting.NAME:
                    v = target_type[v]
                else:
                    raise EncodingSettingException(
                        f"Unexpected enum encoding type: {self._enum_encoding_setting()}"
                    )
            setattr(self, k, v)
        return self

    def to_dict(self):
        dct = dict()
        for k, v in self.__dict__.items():
            if isinstance(v, Iterable) and not isinstance(v, str):
                vals = list()
                for val in v:
                    if isinstance(val, DataClassPlus):
                        vals.append(val.to_dict())
                        continue
                    vals.append(val)
                dct[k] = vals
                continue
            elif isinstance(v, DataClassPlus):
                dct[k] = v.to_dict()
                continue
            elif isinstance(v, Enum):
                if self._enum_encoding_setting() == EnumEncodingSetting.VALUE:
                    v = v.value
                elif self._enum_encoding_setting() == EnumEncodingSetting.NAME:
                    v = v.name
                else:
                    raise EncodingSettingException(
                        f"Unexpected enum encoding type: {self._enum_encoding_setting()}"
                    )
            dct[k] = v
        return dct

    @staticmethod
    def _enum_encoding_setting():
        """
        Override this to return EnumEncodingSetting.NAME if you want enum names instead of values.
        :return: EnumEncodingSetting.
        """
        return EnumEncodingSetting.VALUE

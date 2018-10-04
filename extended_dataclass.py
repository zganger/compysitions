from dataclasses import *


def fromdict(cls, dict_obj):
    args = tuple(dict_obj[key] for key in cls.__annotations__.keys())
    return cls(*args)

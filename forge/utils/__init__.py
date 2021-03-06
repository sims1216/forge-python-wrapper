from __future__ import absolute_import

from json import dumps

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


from .logger import Logger  # noqa

try:
    from .query import Query  # noqa
except ImportError:
    pass


def pretty_print(obj):
    """ """
    try:
        print(dumps(obj, sort_keys=True, indent=4))
    except Exception:
        if isinstance(obj, Iterable):
            for item in obj:
                pretty_print(item)
        else:
            print(obj)

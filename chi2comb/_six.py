import sys

PY2 = sys.version_info[0] == 2


def py2py3_repr(klass):
    if "__repr__" not in klass.__dict__:
        raise ValueError(
            "@py2py3_repr cannot be applied "
            "to %s because it doesn't define __repr__()." % klass.__name__
        )
    klass.__str__ = klass.__repr__

    if PY2:
        klass.__unicode__ = klass.__str__
        klass.__str__ = lambda self: self.__unicode__().encode("utf-8")

    return klass

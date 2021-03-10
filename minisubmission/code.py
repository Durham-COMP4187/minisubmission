import abc


class AbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def type(self): """Return type of self."""

    @abc.abstractproperty
    def name(self): """Return name of class as a string"""
class String(AbstractClass):
    """A class of strings.

    :meth:`type` should return `str`
    :attr:`name` should return 'string'
    """
    pass

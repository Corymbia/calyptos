# stevedore/example/base.py
import abc

import six


@six.add_metaclass(abc.ABCMeta)
class DeployerPlugin(object):
    """Base class for example plugin used in the tutorial.
    """

    @abc.abstractmethod
    def prepare(self, roles):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        :returns: Iterable producing the formatted text.
        """

    @abc.abstractmethod
    def bootstrap(self, roles):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        :returns: Iterable producing the formatted text.
        """

    @abc.abstractmethod
    def provision(self, roles):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        :returns: Iterable producing the formatted text.
        """

    @abc.abstractmethod
    def uninstall(self, roles):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        :returns: Iterable producing the formatted text.
        """
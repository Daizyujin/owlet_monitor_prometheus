from abc import ABCMeta, abstractmethod
from .. import OwletStatus


class BaseExporter():

    @abstractmethod
    def export(self, status: any):
        pass

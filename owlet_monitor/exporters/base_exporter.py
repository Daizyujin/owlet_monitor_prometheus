from abc import ABCMeta, abstractmethod
from ..owlet_status import OwletStatus


class BaseExporter():

    @abstractmethod
    def export(self, status: any):
        pass

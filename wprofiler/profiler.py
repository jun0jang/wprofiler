from abc import ABC, abstractmethod


class Profiler(ABC):
    """ Adapter """

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

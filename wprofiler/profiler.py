from abc import ABC, abstractmethod
from typing import Any


class Profiler(ABC):
    """ Adapter """

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_original(self) -> Any:
        pass

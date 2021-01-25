from abc import ABC, abstractmethod

from wprofiler.profiler import Profiler


class ProfilerFactory(ABC):
    @abstractmethod
    def create(self) -> Profiler:
        pass

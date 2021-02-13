import io
from abc import ABC, abstractmethod

from wprofiler.profiler import Profiler


class StreamFactory(ABC):
    @abstractmethod
    def create(self, profiler: Profiler) -> io.BufferedIOBase:
        pass

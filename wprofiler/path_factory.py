from abc import ABC, abstractmethod

from wprofiler.wsgi_types import Environ


class PathFactory(ABC):
    @abstractmethod
    def create(self, environ: Environ) -> str:
        pass

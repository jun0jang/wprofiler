from pyinstrument.profiler import Profiler as _PyProfiler

from wprofiler import ProfilerFactory
from wprofiler.pyinstrument.profiler import PyinstrumentProfiler


class PyinstrumentProfilerFactory(ProfilerFactory):
    def create(self) -> PyinstrumentProfiler:
        profile = _PyProfiler()
        return PyinstrumentProfiler(profile)

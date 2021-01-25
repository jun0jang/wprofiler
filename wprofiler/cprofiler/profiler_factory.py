from cProfile import Profile

from wprofiler import ProfilerFactory
from wprofiler.cprofiler.profiler import CProfiler


class CProfilerFactory(ProfilerFactory):
    def create(self) -> CProfiler:
        profile = Profile()
        return CProfiler(profile)

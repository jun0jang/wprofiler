import cProfile

from wprofiler.profiler import Profiler


class CProfiler(Profiler):
    def __init__(self, profile: cProfile.Profile):
        self.profile = profile

    def start(self) -> None:
        self.profile.enable()

    def stop(self) -> None:
        self.profile.disable()

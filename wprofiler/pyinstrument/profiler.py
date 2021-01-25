import pyinstrument

from wprofiler.profiler import Profiler


class PyinstrumentProfiler(Profiler):
    def __init__(self, profiler: pyinstrument.Profiler):
        self.profiler = profiler

    def start(self):
        self.profiler.start()

    def stop(self):
        self.profiler.stop()

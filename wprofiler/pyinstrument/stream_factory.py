import io

from pyinstrument.profiler import Profiler as PyProfiler

from wprofiler import StreamFactory
from wprofiler.profiler import Profiler


class PyOutputTextStreamFactory(StreamFactory):
    def __init__(
        self,
        unicode: bool = False,
        color: bool = False,
        show_all: bool = False,
        timeline: bool = False,
    ):
        self.unicode = unicode
        self.color = color
        self.show_all = show_all
        self.timeline = timeline

    def create(self, profiler: Profiler) -> io.BufferedIOBase:
        py_profiler: PyProfiler = profiler.get_original()
        text = py_profiler.output_text(
            unicode=self.unicode,
            color=self.color,
            show_all=self.show_all,
            timeline=self.timeline,
        )

        stream = io.BytesIO(text.encode("utf-8"))
        return stream

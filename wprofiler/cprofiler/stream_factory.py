import io
import pstats
from typing import Iterable, Union

from wprofiler import StreamFactory
from wprofiler.profiler import Profiler


class PstatsStreamFactory(StreamFactory):
    def __init__(
        self,
        sort_keys: Iterable[str] = (),
        amount: Iterable[Union[float, str]] = (),
    ):
        self.sort_keys = list(sort_keys)
        self.amount = list(amount)

    def create(self, profiler: Profiler) -> io.BufferedIOBase:
        profile = profiler.get_original()
        stream = io.BytesIO()
        wrapper = io.TextIOWrapper(stream, encoding="utf-8")

        ps = pstats.Stats(profile, stream=wrapper).sort_stats(*self.sort_keys)
        ps.print_stats(*self.amount)
        wrapper.flush()
        wrapper.detach()

        stream.seek(0)
        return stream

from unittest.mock import patch

from pyinstrument.profiler import Profiler as PyProfiler

from wprofiler.pyinstrument.profiler_factory import PyinstrumentProfilerFactory
from wprofiler.pyinstrument.stream_factory import PyOutputTextStreamFactory


def test_output_text_should_be_file():
    # given
    profiler = PyinstrumentProfilerFactory().create()
    profiler.start()
    profiler.stop()
    excepted_contents = profiler.get_original().output_text()

    # when
    stream = PyOutputTextStreamFactory().create(profiler)

    # then
    assert stream.read().decode("utf-8") == excepted_contents


def test_should_send_output_text_argument():
    # given
    profiler = PyinstrumentProfilerFactory().create()

    excepted_called = dict(
        unicode=True, color=True, show_all=True, timeline=True
    )
    stream_factory = PyOutputTextStreamFactory(**excepted_called)

    # when
    with patch.object(PyProfiler, "output_text", return_value="") as mocked:
        stream_factory.create(profiler)

    # then
    mocked.assert_called_once_with(**excepted_called)

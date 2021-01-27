from unittest.mock import patch

from pyinstrument import Profiler

from wprofiler.pyinstrument.profiler import PyinstrumentProfiler


@patch.object(Profiler, "start")
def test_should_call_start(mocked_start):
    # given
    profiler = PyinstrumentProfiler(Profiler())

    # when
    profiler.start()

    # then
    assert mocked_start.called


@patch.object(Profiler, "stop")
def test_should_call_stop(mocked_stop):
    # given
    profiler = PyinstrumentProfiler(Profiler())

    # when
    profiler.stop()

    # then
    assert mocked_stop.called


def test_get_original():
    # given
    excepted = Profiler()
    profiler = PyinstrumentProfiler(excepted)

    # when
    original = profiler.get_original()

    # then
    assert original is excepted

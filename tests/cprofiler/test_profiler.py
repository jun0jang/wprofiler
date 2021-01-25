from cProfile import Profile
from unittest.mock import patch

from wprofiler.cprofiler.profiler import CProfiler


@patch.object(Profile, "enable")
def test_should_call_enable(mocked_enable):
    # given
    profiler = CProfiler(Profile())

    # when
    profiler.start()

    # then
    assert mocked_enable.called


@patch.object(Profile, "disable")
def test_should_call_disable(mocked_disable):
    # given
    profiler = CProfiler(Profile())

    # when
    profiler.stop()

    # then
    assert mocked_disable.called

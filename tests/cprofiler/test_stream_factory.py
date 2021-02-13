import io
import pstats
from cProfile import Profile
from unittest.mock import patch

import pytest

from wprofiler.cprofiler.profiler_factory import CProfilerFactory
from wprofiler.cprofiler.stream_factory import PstatsStreamFactory


def test_profile_should_be_file():
    # given
    profiler = CProfilerFactory().create()
    profiler.start()
    profiler.stop()
    profile: Profile = profiler.get_original()

    stream = io.StringIO()
    pstats.Stats(profile, stream=stream).sort_stats().print_stats()
    excepted_contents = stream.getvalue()

    # when
    stream = PstatsStreamFactory().create(profiler)

    # then
    assert stream.read().decode("utf-8") == excepted_contents


@pytest.mark.parametrize(
    "sort_keys",
    [
        [pstats.SortKey.CUMULATIVE],
        [pstats.SortKey.CUMULATIVE, pstats.SortKey.LINE],
        [pstats.SortKey.CALLS],
    ],
)
def test_should_be_sorted(sort_keys):
    # given
    profiler = CProfilerFactory().create()
    profiler.start()
    profiler.stop()

    stream_factory = PstatsStreamFactory(sort_keys=sort_keys)

    # when
    with patch.object(pstats.Stats, "sort_stats") as mocked_sort_stats:
        stream_factory.create(profiler)

    # then
    mocked_sort_stats.assert_called_once_with(*sort_keys)


@pytest.mark.parametrize(
    "amount",
    [
        [100],
        [0.5, "__init__"],
    ],
)
def test_should_be_restricted(amount):
    # given
    profiler = CProfilerFactory().create()
    profiler.start()
    profiler.stop()

    stream_factory = PstatsStreamFactory(amount=amount)

    # when
    with patch.object(pstats.Stats, "print_stats") as mocked_print_stats:
        stream_factory.create(profiler)

    # then
    mocked_print_stats.assert_called_once_with(*amount)

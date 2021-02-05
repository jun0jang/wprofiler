from unittest.mock import patch

from pyinstrument.profiler import Profiler as PyProfiler

from wprofiler.pyinstrument.file_factory import (
    PyinstrumentOutputTextFileFactory,
)
from wprofiler.pyinstrument.profiler_factory import PyinstrumentProfilerFactory


def test_output_text_should_be_file():
    # given
    profiler = PyinstrumentProfilerFactory().create()
    profiler.start()
    profiler.stop()
    excepted_contents = profiler.get_original().output_text()

    # when
    file = PyinstrumentOutputTextFileFactory().create(profiler)

    # then
    assert file.read().decode("utf-8") == excepted_contents


def test_should_send_output_text_argument():
    # given
    profiler = PyinstrumentProfilerFactory().create()

    excepted_called = dict(
        unicode=True, color=True, show_all=True, timeline=True
    )
    file_factory = PyinstrumentOutputTextFileFactory(**excepted_called)

    # when
    with patch.object(PyProfiler, "output_text", return_value="") as mocked:
        file_factory.create(profiler)

    # then
    mocked.assert_called_once_with(**excepted_called)

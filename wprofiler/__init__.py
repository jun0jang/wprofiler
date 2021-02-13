from typing import Any, Callable, Dict, Iterable, List, Tuple

from wprofiler.profiler_factory import ProfilerFactory
from wprofiler.stream_factory import StreamFactory

Environ = Dict[str, Any]
Headers = List[Tuple[str, str]]
StartResponse = Callable[[str, Headers], None]
Response = Iterable[bytes]
WSGIApplication = Callable[[Environ, StartResponse], Response]


class WSGIProfiler:
    def __init__(
        self,
        wsgi: WSGIApplication,
        profiler_factory: ProfilerFactory,
        stream_factory: StreamFactory,
        file_storage,
        profile_permission,
    ):
        self.wsgi = wsgi
        self.profiler_factory = profiler_factory
        self.stream_factory = stream_factory
        self.file_storage = file_storage
        self.profile_permission = profile_permission

    def __call__(
        self, environ: Environ, start_response: StartResponse
    ) -> Response:
        if not self.profile_permission.can_profile(environ):
            return self.wsgi(environ, start_response)

        profiler = self.profiler_factory.create()
        profiler.start()
        try:
            respiter = self.wsgi(environ, start_response)
            return respiter
        finally:
            profiler.stop()
            stream = self.stream_factory.create(profiler)
            self.file_storage.save(stream)

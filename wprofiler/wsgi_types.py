from typing import Any, Callable, Dict, Iterable, List, Tuple

Environ = Dict[str, Any]
Headers = List[Tuple[str, str]]
StartResponse = Callable[[str, Headers], None]
Response = Iterable[bytes]
WSGIApplication = Callable[[Environ, StartResponse], Response]

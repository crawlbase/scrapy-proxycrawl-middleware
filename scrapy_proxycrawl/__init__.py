try:
    # Python 2
    from proxycrawl import ProxyCrawlMiddleware
    from request import ProxyCrawlRequest
    from response import ProxyCrawlResponse, ProxyCrawlTextResponse
except ImportError:
    # Python 3
    from .proxycrawl import ProxyCrawlMiddleware
    from .request import ProxyCrawlRequest

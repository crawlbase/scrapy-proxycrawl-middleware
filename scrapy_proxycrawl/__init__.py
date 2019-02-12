try:
    # Python 2
    from proxycrawl import ProxyCrawlMiddleware
except ImportError:
    # Python 3
    from .proxycrawl import ProxyCrawlMiddleware

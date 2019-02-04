try:
    # Python 2
    from proxycrawl import ProxyCrawlMiddleware
except ModuleNotFoundError:
    # Python 3
    from .proxycrawl import ProxyCrawlMiddleware

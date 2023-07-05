# Deprecation warning
def deprecation_warning():
    message = """
    ================================================================================
    DEPRECATION WARNING - 'scrapy-proxycrawl-middleware'
    ================================================================================

    'scrapy-proxycrawl-middleware' is deprecated and will not be maintained. Please switch to 'scrapy-crawlbase-middleware'.

    More details and migration guide: https://github.com/crawlbase-source/scrapy-crawlbase-middleware
    ================================================================================
    """
    print(message)

deprecation_warning()

try:
    # Python 2
    from proxycrawl import ProxyCrawlMiddleware
    from request import ProxyCrawlRequest
    from response import ProxyCrawlResponse, ProxyCrawlTextResponse
except ImportError:
    # Python 3
    from .proxycrawl import ProxyCrawlMiddleware
    from .request import ProxyCrawlRequest

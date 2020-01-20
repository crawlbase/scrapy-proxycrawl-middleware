import logging
from .request import ProxyCrawlRequest

try:
    # For Python 3.0 and later
    from urllib.parse import quote_plus
except ImportError:
    # Fall back to Python 2's
    from urllib import quote_plus

log = logging.getLogger('scrapy.proxycrawl')


class ProxyCrawlMiddleware(object):
    def __init__(self, settings):
        self.proxycrawl_enabled = settings.get('PROXYCRAWL_ENABLED', True)
        self.proxycrawl_token = settings.get('PROXYCRAWL_TOKEN')
        self.proxycrawl_url = 'https://api.proxycrawl.com'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        """Process a request using the proxycrawl API if applicable"""

        if not self.proxycrawl_enabled:
            log.warning('Skipping ProxyCrawl API CALL disabled!')
            return None

        if not isinstance(request, ProxyCrawlRequest):
            return None

        if self.proxycrawl_url not in request.url:
            new_url = self._get_proxied_url(request.url, request.query_params_str)
            log.debug('Using ProxyCrawl API, Request overridden with URL: {}'.format(new_url))
            return request.replace(url=new_url)

    def process_response(self, request, response, spider):
        """Process a response coming from proxycrawl API if applicable"""

        if not isinstance(request, ProxyCrawlRequest):
            return response

        # Replace url again with the original url saved in request
        log.debug('Using ProxyCrawl API, Response overridden with URL: {}'.format(request.original_url))
        return response.replace(url=request.original_url)

    def _get_proxied_url(self, url, query_params):
        """
        Transform the url into a call to proxy crawl api, sending the target url as query parameter.
        """
        original_url_encoded = quote_plus(url, safe='')
        proxycrawl_url = self.proxycrawl_url
        proxycrawl_token = self.proxycrawl_token
        proxycrawl_query_params = query_params
        proxied_url = '{}/?token={}&{}&url={}'.format(
            proxycrawl_url,
            proxycrawl_token,
            proxycrawl_query_params,
            original_url_encoded
        )
        return proxied_url

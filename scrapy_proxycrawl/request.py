import urllib
import urllib.parse
import copy
from json import JSONEncoder
from scrapy import Request


class ProxyCrawlRequest(Request):
    """Scrapy ``Request`` subclass providing additional arguments for Proxy Crawl"""

    def __init__(self, url, original_url=None, response_format='html', user_agent=None, page_wait=None, ajax_wait=False,
                 css_click_selector=None, device='desktop', get_cookies=False,
                 get_headers=False, proxy_session=None, cookies_session=None,
                 screenshot=False, scraper=None, autoparse=False, country=None, **kwargs):
        """
        Initialize a new request

        Docs: https://proxycrawl.com/dashboard/api/docs

        response_format: str
            Indicates the response response_format, either json or html. Defaults to html
        user_agent: str
            If you want to make the request with a custom user agent, you can pass it here
        page_wait: int
            If you are using the javascript token, you can optionally pass page_wait parameter to wait
            an amount of milliseconds before the browser captures the resulting html code.
        ajax_wait: boolean
            If you are using the javascript token, you can optionally pass ajax_wait parameter to wait
            for the ajax requests to finish before getting the html response.
        css_click_selector: str
            If you are using the javascript token, you can optionally pass css_click_selector
            parameter to click an element in the page before the browser captures the resulting html code.
        device: str
            Optionally, if you don't want to specify a user_agent but you want to have the requests from
            a specific device, you can use this parameter. There are two options available: desktop and mobile.
        get_cookies: boolean
            Optionally, if you need to get the cookies that the original website sets on the response,
            you can use the get_cookies=True parameter
        get_headers: boolean
            Optionally, if you need to get the headers that the original website sets on the response,
            you can use the get_headers=True parameter.
        proxy_session: str
            If you need to use the same proxy for subsequent requests, you can use the
            proxy_session parameter. The &proxy_session= parameter can be any value. Simply send a new value to create a
            new proxy session (this will allow you to continue using the same proxy for all subsequent requests with
            that proxy session value). Sessions expire 30 seconds after the last API call.
        cookies_session: str
            If you need to send the cookies that come back on every request to all subsequent calls,
            you can use the &cookies_session= parameter. The cookies_session parameter can be any value. Simply send a
            new value to create a new cookies session (this will allow you to send the returned cookies from the
            subsequent calls to the next API calls with that cookies session value).
            Sessions expire in 300 seconds after the last API call.
        screenshot: boolean
            If you are using the javascript token, you can optionally pass &screenshot=true parameter to
            get a screenshot in JPEG response_format of the whole crawled page. ProxyCrawl will send you back the screenshot_url
            in the response headers (or in the json response if you use &response_format=json). The screenshot_url expires in
            one hour.
        scraper: str
            Returns back the information parsed according to the specified scraper. Check the list of all
            the available data scrapers to see which one to choose. The response will come back as JSON.
            If you don't use it, you will receive back the full HTML of the page so you can scrape it freely.
        autoparse: boolean
            Optionally, if you need to get the scraped data of the page that you requested, you can pass
            autoparse=True parameter. The response will come back as JSON. The structure of the response varies
            depending on the URL that you sent. autoparse is an optional parameter. If you don't use it, you will
            receive back the full HTML of the page so you can scrape it freely.
        country: str
            If you want your requests to be geolocated from a specific country, you can use the country
            parameter, like country='US' (two-character country code). Please take into account that specifying a
            country can reduce the amount of successful requests you get back, so use it wisely and only when
            geolocation crawls are required.

        :param args: other args to be passed to Scrapy base Request constructor
        :param kwargs: other kwargs to be passed to Scrapy base Request constructor
        """
        self.original_url = original_url if original_url else url  # Save url to replace it in response later
        self.response_format = response_format
        self.user_agent = user_agent
        self.page_wait = page_wait
        self.ajax_wait = ajax_wait
        self.css_click_selector = css_click_selector
        self.device = device
        self.get_cookies = get_cookies
        self.get_headers = get_headers
        self.proxy_session = proxy_session
        self.cookies_session = cookies_session
        self.screenshot = screenshot
        self.scraper = scraper
        self.autoparse = autoparse
        self.country = country
        self.query_params_str=self._build_query_params()
        super().__init__(url, **kwargs)

    def replace(self, *args, **kwargs):
        """Create a new Request with the same attributes except for those
        given new values.
        """
        for x in ['url', 'original_url', 'response_format', 'user_agent', 'page_wait',
                  'ajax_wait', 'css_click_selector', 'device', 'get_cookies', 'get_headers',
                  'proxy_session', 'cookies_session', 'screenshot', 'scraper', 'autoparse',
                  'country', 'method', 'headers', 'body', 'cookies', 'meta', 'flags',
                  'encoding', 'priority', 'dont_filter', 'callback', 'errback', 'cb_kwargs']:
            kwargs.setdefault(x, getattr(self, x))
        cls = kwargs.pop('cls', self.__class__)
        return cls(*args, **kwargs)

    def _build_query_params(self):
        encoder = JSONEncoder()
        # Prepare aprams from attributes
        params = copy.deepcopy(self.__dict__)
        params.pop('original_url')  # Remove param
        params['format'] = params.pop('response_format')  # rename param
        # Convert values proxy crawl compatible values (json-like, i.e True -> 'true')
        # and ignore params with None or False value
        params = [(k, encoder.encode(v).strip('"')) for k,v in params.items() if v]
        # Make query string
        query_params = urllib.parse.urlencode(params)
        return query_params


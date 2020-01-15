# -*- coding: utf-8 -*-
from __future__ import absolute_import

from scrapy.http import Response, TextResponse


class _ProxyCrawlResponseMixin(object):
    """
    This mixin fixes response.url and adds response.original_url
    """
    def __init__(self, url, *args, **kwargs):
        # proxied_url = kwargs.pop('proxied_url', None)
        # if proxied_url is not None:
        #     self.proxied_url = proxied_url
        # else:
        #     self.proxied_url = None
        super(_ProxyCrawlResponseMixin, self).__init__(url, *args, **kwargs)

    def replace(self, *args, **kwargs):
        """Create a new Response with the same attributes except for those
        given new values.
        """
        for x in ['url', 'status', 'headers', 'body', 'request', 'flags']:  #, 'proxied_url'
            kwargs.setdefault(x, getattr(self, x))
        cls = kwargs.pop('cls', self.__class__)
        return cls(*args, **kwargs)


class ProxyCrawlResponse(_ProxyCrawlResponseMixin, Response):
    """
    This Response subclass sets response.url to the URL of a remote website
    instead of an URL of ProxyCrawl api. "Real" response URL is still available
    as ``response.proxied_url``.
    """


class ProxyCrawlTextResponse(_ProxyCrawlResponseMixin, TextResponse):
    """
    This TextResponse subclass sets response.url to the URL of a remote website
    instead of an URL of ProxyCrawl api. "Real" response URL is still available
    as ``response.proxied_url``.
    """
    def replace(self, *args, **kwargs):
        kwargs.setdefault('encoding', self.encoding)
        return _ProxyCrawlResponseMixin.replace(self, *args, **kwargs)
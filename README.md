# DEPRECATION NOTICE

> :warning: **IMPORTANT:** This package is no longer maintained or supported. For the latest updates, please use our new package at [scrapy-crawlbase-middleware](https://github.com/crawlbase-source/scrapy-crawlbase-middleware).

---

# ProxyCrawl API middleware for Scrapy

Processes [Scrapy](http://scrapy.org/) requests using [ProxyCrawl](https://proxycrawl.com) services either with Normal or Javascript tokens

## Installing

Choose a way of installing:

- Clone the repository inside your Scrapy project and run the following:

```bash
python setup.py install
```

- Or use [PyPi](https://pypi.org/project/scrapy-proxycrawl-middleware/) Python package manager. `pip install scrapy-proxycrawl-middleware`

Then in your Scrapy `settings.py` add the following lines:

```python
# Activate the middleware
PROXYCRAWL_ENABLED = True

# The ProxyCrawl API token you wish to use, either normal of javascript token
PROXYCRAWL_TOKEN = 'your token'

# Enable the middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy_proxycrawl.ProxyCrawlMiddleware': 610
}
```

## Usage

Use the scrapy_proxycrawl.ProxyCrawlRequest instead of the scrapy built-in Request.
The scrapy_proxycrawl.ProxyCrawlRequest accepts additional arguments, used in Proxy Crawl API:

```python
from scrapy_proxycrawl import ProxyCrawlRequest

class ExampleScraper(Spider):

    def start_requests(self):
        yield ProxyCrawlRequest(
            "http://target-url",
            callback=self.parse_result
            device='desktop',
            country='US',
            page_wait=1000,
            ajax_wait=True,
            dont_filter=True
        )
```

The target url will be replaced with proxy crawl url and parameters will be encoded into the url by the middleware automatically.

If you have questions or need help using the library, please open an issue or [contact us](https://proxycrawl.com/contact).

---

Copyright 2023 ProxyCrawl

# ProxyCrawl API middleware for Scrapy

Processes [Scrapy](http://scrapy.org/) requests using [ProxyCrawl](https://proxycrawl.com) services either with Normal or Javascript tokens


## Installation

Clone the repository inside your Scrapy project and run the following:

```bash
python setup.py install
```

In your Scrapy `settings.py` add the following lines:

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

If you have questions or need help using the library, please open an issue or [contact us](https://proxycrawl.com/contact).

---

Copyright 2019 ProxyCrawl

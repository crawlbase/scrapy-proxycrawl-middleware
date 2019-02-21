"""ProxyCrawl Scrapy middleware."""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

readme = open('README.md').read()

setup(
    name = 'scrapy-proxycrawl-middleware',
    license = 'Apache-2.0',
    version = '1.0.2',
    description = 'Scrapy ProxyCrawl Proxy Middleware: ProxyCrawl interfacing middleware for Scrapy',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'ProxyCrawl',
    author_email = 'info@proxycrawl.com',
    url = 'https://github.com/proxycrawl/scrapy-proxycrawl-middleware',
    keywords = 'scrapy middleware scraping scraper crawler crawling proxycrawl api',
    include_package_data = True,
    packages = find_packages(),
    classifiers = (
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    )
)

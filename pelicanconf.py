#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Ubucon Team'
SITENAME = 'Ubucon'
SITEURL = ''

#MENUITEMS = (
#                ('Archiv', ),
#            )

DEFAULT_LANG = 'de'
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a, %-d. %B %Y'
CURRENTYEAR = date.today().year

SUMMARY_MAX_LENGTH = 50

PATH = 'content'
IGNORE_FILES = ['.#*', 'files']
STATIC_PATHS = ['files']
THEME = 'theme'

JINJA_ENVIRONMENT = {'trim_blocks': True,
                     'lstrip_blocks': True,
                     'extensions': ['jinja2.ext.ExprStmtExtension',]}

## Plugins ##

LOCALE = 'de_DE.utf-8' # for open_graph

PLUGIN_PATHS = ['plugins']
PLUGINS = [
#            'pelican-page-order',
            'assets',
#            'pelican-open_graph',
            'sitemap',
          ]

ASSET_SOURCE_PATHS = [
    'vendor',
]

SITEMAP = {
    'format': 'xml',
    }

# only one RSS Feed with all news
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 20
RSS_FEED_SUMMARY_ONLY = False

FEED_RSS = 'rss.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_RSS = None
TAG_FEED_ATOM = None


## Pagination ##

DEFAULT_PAGINATION = 5

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

## URL-settings ##

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

INDEX_SAVE_AS = 'index.html'

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

ARTICLE_LANG_URL = ARTICLE_URL + '{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

# author, categories and tags should not been generated
AUTHORS_SAVE_AS = AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_URL = TAG_SAVE_AS = ''
TAGS_URL = TAGS_SAVE_AS = ''

SOCIAL = (
    ('facebook', 'https://www.facebook.com/Ubucon'),
    ('Google+', 'https://plus.google.com/b/101157317074955454980/101157317074955454980/posts'),
    ('twitter', 'https://twitter.com/Ubucon'),
    ('YouTube', ('http://www.youtube.com/ubuconde')
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

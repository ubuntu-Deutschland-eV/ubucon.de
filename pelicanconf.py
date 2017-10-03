#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Ubucon Team'
SITENAME = 'Ubucon Deutschland'
SITEURL = ''
SOCIAL = (
    ('facebook', 'https://www.facebook.com/Ubucon'),
    ('Google+', 'https://plus.google.com/b/101157317074955454980/101157317074955454980/posts'),
    ('twitter', 'https://twitter.com/Ubucon'),
    ('YouTube', ('http://www.youtube.com/ubuconde'))
)

MENUITEMS = (
#               (description, link),
                ('Archiv', 'archiv'),
            )
DISPLAY_PAGES_ON_MENU = False

LOCALE = 'de_DE.utf-8'
DEFAULT_LANG = 'de'
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a, %-d. %B %Y'
CURRENTYEAR = date.today().year

SUMMARY_MAX_LENGTH = 50

PATH = 'content'
IGNORE_FILES = ['.#*', 'files', '__pycache__']
STATIC_PATHS = ['files']
PAGE_PATHS = ['pages']
THEME = 'themes/verein'

JINJA_ENVIRONMENT = {'trim_blocks': True,
                     'lstrip_blocks': True,
                     'extensions': ['jinja2.ext.ExprStmtExtension',]}

REVERSE_CATEGORY_ORDER = True

## Plugins ##

PLUGIN_PATHS = ['plugins']
PLUGINS = [
#            'autopages', # , currently wont work with pelican-page-hierarchy
            'pelican-page-hierarchy',
            'assets',
            'sitemap',
          ]


PATH_METADATA = 'pages/(?P<path>.*)\..*'

## for autopages
#CATEGORY_PAGE_PATH = 'content/category_descriptions'
#ARTICLE_EXCLUDES = PAGE_EXCLUDES = ['category_descriptions']

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
CATEGORY_FEED_RSS = '%s.rss.xml'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_RSS = None
TAG_FEED_ATOM = None


## Pagination ##

DEFAULT_PAGINATION = 7

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

## URL-settings ##

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

INDEX_URL = INDEX_SAVE_AS = ''

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

ARTICLE_LANG_URL = ARTICLE_URL + '{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

CATEGORIES_SAVE_AS = 'archiv/index.html'

# author and tags should not been generated
AUTHORS_SAVE_AS = AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_URL = TAG_SAVE_AS = ''
TAGS_URL = TAGS_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

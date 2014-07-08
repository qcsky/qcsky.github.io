#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'qcsky'
SITENAME = u"qcsky's blog"
SITESUBTITLE = u'Nothing is impossible'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Title menu
MENUITEMS = [
				('Home', '/'),
				('Archives', '/archives.html')
			]

NEWST_FIRST_ARCHIVES = True

# URL settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', '#'),
          ('Facebook', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'pelican-theme/pelican-octopress-theme/'

# Plugin
PLUGIN_PATHS = ['pelican-plugins',]
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.include_code',
			'liquid_tags.literal'
			]

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'downloads', 'favicon.png', 'README.md', 'googled5535dfb6f169df8.html']

# Search
SEARCH_BOX = True

# QR Code generation
QR_CODE = True

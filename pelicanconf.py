#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Trent Palmer'
SITENAME = 'Attention Span History'
SITEURL = 'https://blog.trentpalmer.org'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SOCIAL_WIDGET_NAME = 'follow'

# Blogroll
LINKS = (('Doc Blog', 'https://blog.trentsonlinedocs.xyz/'),
         ('Favorite Podcasts', 'https://blog.trentsonlinedocs.xyz/posts/trents-favorite-podcasts/'),
         ('TrentReads', 'https://trentpalmer.org'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/boringtrent'),
          ('github', 'https://github.com/TrentSPalmer'),)

MENUITEMS = (('Twitter', 'https://twitter.com/boringtrent'),
             ('Github', 'https://github.com/TrentSPalmer'),
             ('Doc Blog', 'https://blog.trentsonlinedocs.xyz/'),
             ('Favorite Podcasts', 'https://blog.trentsonlinedocs.xyz/posts/trents-favorite-podcasts/'),
             ('TrentReads', 'https://trentpalmer.org'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/bstrapplus"

SUMMARY_MAX_LENGTH = 30

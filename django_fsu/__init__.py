'''
Flask-Style URL Patterns for Django.

The module intends to provide a way to write URL patterns without regex.

For the syntax of Flask routing URLs, see:
http://flask.pocoo.org/docs/latest/api/#url-route-registrations
'''
import re
import itertools

from django.conf.urls import url as django_url


__version__ = '0.1.1'


quote = re.compile(r'\<([^<>]+)\>')


formatters = {
    'string': r'[^\/]+',
    'int': r'\d+',
    'float': r'[+-]?(?:\d+\.?\d*|\d*\.\d+|[Ii][Nn][Ff]|[Nn][Aa][Nn])',
    'uuid': r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',  # noqa
    'path': r'.+',
}


def make_regex(spec):
    '''
    convert a flask-style <spec> into django regex.

    "formatter:keyword" gives:
        (?P<keyword>formatter_to_regex)
    "keyword":
        this defaults formatter to 'string'
    '''
    fstring, delim, keyword = spec.rpartition(':')
    formatter = formatters[fstring or 'string']
    return r'(?P<{keyword}>{regex})'.format(keyword=keyword, regex=formatter)


def iroute(path):
    for fragment, func in zip(
        quote.split(path),
        itertools.cycle([re.escape, make_regex])
    ):
        yield func(fragment)


def route(path):
    '''
    convert a flask-style url to django's regex,
    without the starting '^' or ending '/'.
    '''
    return ''.join(iroute(path))


def url(path, view, *args, **kwargs):
    '''
    wrapper of django.conf.urls.url,
    but excepts flask-style url instead of regex as the first argument
    '''
    if callable(view):
        func = endpoint_url
    elif isinstance(view, (list, tuple)):
        func = include_url
    else:
        raise TypeError('Invalid view %r of type %r' % (view, type(view)))
    return func(path, view, *args, **kwargs)


def endpoint_url(path, *args, **kwargs):
    return django_url('^%s$' % route(path), *args, **kwargs)


def include_url(path, *args, **kwargs):
    return django_url('^' + route(path), *args, **kwargs)


endpoint_url.__doc__ = url.__doc__ + '''
    assumes the view is a actual view (not a include(...))'''

include_url.__doc__ = url.__doc__ + '''
    assumes the view is a django.conf.urls.include(...) result'''

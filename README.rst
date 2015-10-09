==========
django-fsu
==========

Flask-Style URL Patterns for Django

------------
Installation
------------

.. code-block:: bash

    pip install django-fsu

-----
Usage
-----

In urls.py: change your regex patterns to flask-styled paths.

.. code-block:: python

    from django.conf.urls import include
    from django_fsu import url

    from . import views

    urlpatterns = [
        url('login', views.login),
        url('user/<username>', views.profile),
        url('article/<int:pk>', views.article),
        url('projects/', include('projects.urls'),
    ]

Variable parts in the route can be specified with angular brackets (``user/<username>``). By default a variable part in the URL accepts a string without a slash however a different format code can be specified as well by using ``<code:name>``.

Variable parts are passed to the view function as keyword arguments. In the above example, ``views.profile`` will be passed with a keyword argument: ``username``.

Currently supported formats codes are:

* ``string`` (the default, accepts string without a slash)
* ``int``
* ``float``
* ``uuid``
* ``path`` (accepts any string)

Please note that ``int`` and ``float`` variables are still passed to the view function as a string.

To see how individual functions work,
see the docstrings or type ``help('django_fsu')`` in the interactive prompt.

Credits to: http://flask.pocoo.org/docs/latest/api/#url-route-registrations.

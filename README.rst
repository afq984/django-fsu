==========
django-fsu
==========

Flask-Style URL Patterns for Django

-----
Usage
-----

In urls.py: change your regex patterns to flask-styled paths

(see format here: http://flask.pocoo.org/docs/latest/api/#url-route-registrations)

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

To see how individual functions work,
see the docstrings or type ``help('django_fsu')`` in the interactive prompt.

------------
Installation
------------

.. code-block:: bash

    pip install django-fsu

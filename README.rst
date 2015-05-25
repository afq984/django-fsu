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
        url('admin/', include('admin.sites.urls'),
    ]

------------
Installation
------------

.. code-block:: bash

    pip install django-fsu

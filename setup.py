from setuptools import setup


setup(
    name='django-fsu',
    version='0.1.1',
    packages=['django_fsu'],
    include_package_data=True,
    license='BSD License',
    description='Flask-Style URL Patterns for Django',
    url='http://github.com/afg984/django-fsu',
    author='afg984',
    author_email='afg984@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)

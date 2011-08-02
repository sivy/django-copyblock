__doc__ = """
Manage website copy as a directory of markdown-formatted files. Insert files as copy into your
Django templates.
"""

from setuptools import setup

setup(
    name='django-copyblock',
    version='0.2.1',
    author='Steve Ivy',
    author_email='steve@wallrazer.com',
    description='Manage website copy as a directory of markdown-formatted files. Insert files as copy into your Django templates.',
    license='MIT License',
    requires=(),
    keywords='django copy markdown',
    url='http://github.com/sivy/django-copyblock/',
    long_description=__doc__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)

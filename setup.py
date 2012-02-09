__doc__ = """
Manage website copy as a directory of markdown-formatted files. Insert files as copy into your
Django templates.
"""

from setuptools import setup, find_packages
import os
from copyblock import VERSION

ld = "\n\n".join(("Copyblock came out of a desire of mine to separate the copy for a site I'm working on from the site templates. Things like welcome messages, intro copy for forms, etc. This is copy I'd like to be able to tweak easily over time without having to redeploy the entire site to make it happen. What I wanted was a system kindof like gettext, but without .po files, the weird syntax, and a separete app to generate the right files.",
      "What I wanted was really simple: a directory of text files, optionally in [Markdown](http://daringfireball.net/projects/markdown), that could be inserted into my app templates with a template tag. That's what Copyblock does."))

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-copyblock',
    version=".".join(map(str, VERSION)),
    author='Steve Ivy',
    author_email='steve@wallrazer.com',
    description='Manage website copy as a directory of markdown-formatted files. Insert files as copy into your Django templates.',
    license='MIT License',
    packages=find_packages(),
    requires=['markdown'],
    keywords='django copy markdown',
    url='http://github.com/sivy/django-copyblock/',
#    long_description=ld,
    long_description=read('README'),
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

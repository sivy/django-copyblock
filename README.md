# Copyblock

Copyblock came out of a desire of mine to separate the copy for a site I'm working on from the site templates. Things like welcome messages, intro copy for forms, etc. This is copy I'd like to be able to tweak easily over time without having to redeploy the entire site to make it happen. What I wanted was a system kindof like gettext, but without .po files, the weird syntax, and a separete app to generate the right files.

What I wanted was really simple: a directory of text files, optionally in [Markdown](http://daringfireball.net/projects/markdown), that could be inserted into my app templates with a template tag. That's what Copyblock does.

## Installation

From Pypi:

    % pip install django-copyblock

From [Github](http://github.comsivy/django-copyblock):

    % pip install -e git://github.com/sivy/django-copyblock.git

## Usage

Create a root directory for your copyblock files:

    %  mkdir copy/dir

Add this path to your settings file:

    COPYBLOCK_ROOT='path/to/your/copy/dir'

In your templates:

    {% copyblock filename %}

This will do the following:

* Look for copy/dir/filename.markdown
* Run the file filename.markdown through markdown
* Cache the output for future lookups
* Insert the output in the rendered template

 Right now, copyblock only does markdown. If your copy is not in markdown (plain text), you can pass in the `nomarkdown` parameter to the template tag:

    {% copyblock filename nomarkdown %}

 Also, if you don't want to use the in-memory cache (load copy from file every time, good for copy editing), pass in the `nocache` parameter:

    {% copyblock filename nocache %}

# @TODO

* Add support for other text formats, or even HTML (suggestions, request? <steve@wallrazer.com>)
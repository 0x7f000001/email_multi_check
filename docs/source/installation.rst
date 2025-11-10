.. _installation:

Installation
============

Requirements
------------

Python 3.11 or newer.

Installation
------------

Many free operating system distributions have dnspython packaged for
you, so you should check there first.

The next easiest option is to use ``pip``::
    
        pip install email-multi-check

If ``pip`` is not available, you can download the latest zip file from
`PyPI <https://pypi.python.org/pypi/email-multi-check/>`_, unzip it.

Or from source::

        pip install .\dist\email_multi_check-1.0.7-py3-none-any.whl

Finally, you have the option of cloning the dnspython source from github
and building it::

        git clone https://github.com/0x7f000001/email_multi_check.git


Optional Modules
----------------

The following modules for full functionality.

``dnspython``
``idna``
``requests``
``pydantic``
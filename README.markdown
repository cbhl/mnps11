mathNEWS Production System
==========================

mathNEWS Production System Rewrite (2011)

Dependencies
------------
- MySQL (sqlite3 might work, but it sucks for concurrency/scaling)
- [MySQL for Python] [http://sourceforge.net/projects/mysql-python]
    - [setuptools] [http://pypi.python.org/pypi/setuptools]
- [Python Imaging Library (PIL)] [http://www.pythonware.com/products/pil]
- [lxml] [http://lxml.de/]
- [pandoc] [http://johnmacfarlane.net/pandoc/]
- [pyandoc] [https://github.com/cbhl/pyandoc] (python bindings for pandoc)
    - [upstream] [https://github.com/kennethreitz/pyandoc] also works but watch the default value of *pandoc.PANDOC_PATH*
- www.student.cs or some other PHP-CGI-enabled on-campus server which can do CAS authentication
- django (development version)
    - clone from the [git mirror] [https://github.com/django/django]
- django-cas


### Installing on Ubuntu Linux
sudo apt-get install mysql-server python-mysqldb python-imaging pandoc python-lxml

You will also need to install pyandoc, django, django-cas into Python's dist-packages:
    1. git clone [https://github.com/django/django.git]
    2. git clone [https://github.com/cbhl/pyandoc.git]
    3. Create files named /usr/lib/python2.7/dist-packages/<package>.pth with the directory of the library
    e.g. /opt/django for django

### Installing on Mac OS X

Left as an exercise for the reader -- patches accepted! You'll probably have to build most of it from scratch.

Pivotal Tracker
---------------
[Pivotal Tracker] [https://www.pivotaltracker.com/projects/322953]

Setting up dev environment
---------------
- Install all dependencies
- Create MySQL user (see settings.py for username/password)
- Create *'mathnews_dev'* table in database
- python manage.py syncdb
- python manage.py runserver

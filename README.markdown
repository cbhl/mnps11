mathNEWS Production System
==========================

mathNEWS Production System Rewrite (2011)

Dependencies
------------
- django
    - python-mysqldb
    - Python Imaging Library
    - MySQL (sqlite3 might work, but it sucks for concurrency/scaling)
- pandoc
- [pyandoc] [https://github.com/cbhl/pyandoc] (python bindings for pandoc)
    - [upstream] [https://github.com/kennethreitz/pyandoc] also works but watch the default value of *pandoc.PANDOC_PATH*
- www.student.cs or some other PHP-CGI-enabled on-campus server which can do CAS authentication

Pivotal Tracker
---------------

[Pivotal Tracker] [https://www.pivotaltracker.com/projects/322953]


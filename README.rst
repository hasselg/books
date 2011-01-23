Description
============
Some information describing *books*.

Dependencies
============
The following dependencies are required for running *books*:

* CherryPy (http://www.cherrypy.org)
* Django (http://www.djangoproject.com)
* PyQt4 (http://www.riverbankcomputing.co.uk/software/pyqt/intro) (required for Clothed Mode)

If your Python installation cannot import the respective modules, then *books* will not be able to run correctly.

Execution
============
*books* has two primary execution modes. The first mode is as a naked web application. The embedded web server is executed and the application is access via one of the available web browsers on the system. The second execution mode is as a desktop application. The desktop application execution mode takes care of starting and stopping the embedded web server, and also provides a basic browser for accessing the application.

Naked Mode
----------
In order to run in naked mode, execute books.py. Then, point your browser to http://localhost:8080/books/library/.

Clothed Mode
------------
In order to run in clothed mode, execute books.pyw.


#!/usr/bin/env python
import os
import sys

import cherry_server as books_server

if __name__ == '__main__':
    # Start the embedded server
    sys.path.append(os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'books.settings'
    server = books_server.Server()
    server.start(block=True)



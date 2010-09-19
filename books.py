import os
import sys
import subprocess

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'books.settings'
    # import twisted_server as s
    import cherry_server as s
    s.main()
    


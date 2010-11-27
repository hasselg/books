import os
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'books.settings'
    import cherry_server as s
    s.main()
    


import sys
from owlet_monitor.owlet_monitor import loop, FatalError

if __name__ == '__main__':
    try:
        loop()
    except FatalError as e:
        sys.stderr.write('%s\n' % e)
        sys.exit(1)

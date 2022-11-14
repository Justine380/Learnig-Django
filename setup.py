import inspect
import sys

def foo():
    print('called from',inspect.getframeinfo(sys.getframe(1)).filename)
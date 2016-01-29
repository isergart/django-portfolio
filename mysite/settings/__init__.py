from .base import *

try:
    from .local import *
except ImportError:
    print("Can't find settings.local! Make it from local.py.template")
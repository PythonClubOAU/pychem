import sys

from tools.errors import VersionError

if sys.version_info <= (2, 7):
    raise VersionError("Pyconvert requires at least python 2.7 to run")

import importlib

minimum_supported_version = "2.7"
required_libraries = ["pyconvert"]

for lib in required_libraries:
    try:
        importlib.import_module(lib)
    except ImportError as error:
        raise ImportError("Pychem requires {0} to run.".format(lib))

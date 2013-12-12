# -*- mode: python -*-
# Django settings for lolyx project.

"""
Main settings for lolix instances.
This file auto load configurations from settings files.

First it load base configuration. base.py contains a default configuration.
Then it try to load a local_settings configuration file. This file will then load on of the custom configuration file (devel_settings, test_settings and so on).

You need to create the local_settings.py file. It should look something like this:

from devel_settings import *

"""

# We try to load custom settings here
from base import *
try:
    from local_settings import *
except:
    pass

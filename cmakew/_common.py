# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import logbook


QUIET_LOG_LEVEL = logbook.NOTSET


class BuildAction(object):
    CMAKE = "cmake"
    RECMAKE = "recmake"
    CLEAN = "clean"
    BUILD = "build"
    REBUILD = "rebuild"

    DEFAULT = BUILD
    LIST = [CMAKE, RECMAKE, CLEAN, BUILD, REBUILD]


class BuildType(object):
    DEBUG = "Debug"
    RELEASE = "Release"

    DEFAULT = DEBUG
    LIST = [DEBUG, RELEASE]

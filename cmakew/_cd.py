# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import

import os

from ._logger import logger


class Cd(object):
    def __init__(self, new_path):
        self.__new_path = os.path.expanduser(new_path)
        self.__saved_path = None

    def __enter__(self):
        self.__saved_path = os.getcwd()
        logger.debug("change directory to {}".format(self.__new_path))
        os.chdir(self.__new_path)

    def __exit__(self, exception_type, exception_value, traceback):
        logger.debug("change directory to {}".format(self.__saved_path))
        os.chdir(self.__saved_path)

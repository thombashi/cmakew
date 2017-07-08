#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import errno
import json
import os
import platform
import sys

import logbook
import six
import subprocrunner
import typepy

from ._cd import Cd
from ._common import BuildAction
from ._compiler import CompilerFactory
from ._logger import (
    logger,
    set_log_level,
)
from ._option import parse_option
from ._visual_studio import vsinfo


logbook.StderrHandler(
    level=logbook.DEBUG,
    format_string="[{record.level_name}] {record.channel}: {record.message}"
).push_application()


class CMakeCommandBuilder(object):

    def __init__(self, options):
        self.__options = options

    def get_cmake_commmand(self):
        cmake_command_list = [
            'cmake ../{:s}'.format(self.__options.source_dir),
            "-DCMAKE_BUILD_TYPE={:s}".format(self.__options.build_type),
        ]

        for key, value in six.iteritems(self.__read_cmake_options()):
            cmake_command_list.append('-D{}={}'.format(key, value))

        generator = self.__get_generator()
        if generator is not None:
            cmake_command_list.append('-G "{:s}"'.format(
                generator))

        return " ".join(cmake_command_list)

    @staticmethod
    def __get_win_generator():
        return "Visual Studio {:d} {:s}".format(
            vsinfo.version_info.major,
            "Win64" if platform.architecture()[0] == "64bit" else ""
        )

    def __get_generator(self):
        if self.__options.generator is not None:
            return self.__options.generator

        system = platform.system()

        if system == "Windows":
            return self.__get_win_generator()
        elif system == "Linux":
            return "Unix Makefiles"
        else:
            return "Unix Makefiles"

        raise NotImplementedError("not supported system: {}".format(system))

    def __read_cmake_options(self):
        file_path = self.__options.cmake_options

        if typepy.is_null_string(file_path):
            logger.debug("no cmake option file designated.")
            return {}

        if not os.path.isfile(file_path):
            logger.debug(
                "cmake option file not found: path='{}'".format(file_path))
            return {}

        with open(file_path) as f:
            cmake_options = json.loads(f.read())

        return cmake_options


def main():
    options = parse_option()
    set_log_level(options.log_level)

    build_dir = options.build_dir
    try:
        compiler = CompilerFactory.create(build_dir)
    except ValueError as e:
        logger.error(e)
        return errno.EINVAL

    if options.action in [BuildAction.CLEAN, BuildAction.REBUILD]:
        result = compiler.clean()

        if options.action == BuildAction.CLEAN:
            return result

    if options.action in [BuildAction.RECMAKE]:
        cmake_cache_path = "/".join([
            compiler.build_dir_path, "CMakeCache.txt"])
        logger.debug("delete {:s}".format(cmake_cache_path))
        os.remove(cmake_cache_path)

    if not os.path.isdir(build_dir):
        logger.debug("make directory: {:s}".format(build_dir))
        os.makedirs(build_dir)

    if options.action in [
            BuildAction.CMAKE, BuildAction.RECMAKE,
            BuildAction.BUILD, BuildAction.REBUILD
    ]:
        command_builder = CMakeCommandBuilder(options)
        runner = subprocrunner.SubprocessRunner(
            command_builder.get_cmake_commmand())

        with Cd(build_dir):
            runner.run()

        if typepy.is_null_string(runner.stderr):
            # cmake will output results to stderr if executed normally

            logger.error(
                "unexpected error occurred: stdout={}".format(runner.stdout))

            return 1

        if runner.returncode == 0:
            logging_func = logger.info
        else:
            logging_func = logger.error

        if typepy.is_not_null_string(runner.stdout):
            logging_func(runner.stdout)

        if typepy.is_not_null_string(runner.stderr):
            logging_func(runner.stderr)

        if runner.returncode != 0:
            return 1

    if options.action in [BuildAction.BUILD, BuildAction.REBUILD]:
        with Cd(build_dir):
            compiler.build()

    return 0


if __name__ == "__main__":
    sys.exit(main())

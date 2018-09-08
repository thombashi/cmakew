# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals

import argparse
from textwrap import dedent

import logbook

from .__version__ import __version__
from ._common import QUIET_LOG_LEVEL, BuildAction, BuildType


DEFAULT_CMAKE_OPTIONS_FILE = "cmake_options.json"


def parse_option():
    description = "A CLI tool for CMake and compiler wrapper."
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description,
        epilog=dedent(
            """\
            Issue tracker: https://github.com/thombashi/cmakew/issues
            """
        ),
    )
    parser.add_argument("-V", "--version", action="version", version="%(prog)s " + __version__)

    parser.add_argument(
        "source_dir", metavar="SOURCE_DIR_PATH", help="""relative path to the source directory."""
    )

    group = parser.add_argument_group("Directory Options")
    group.add_argument(
        "--build-dir",
        default="build",
        help="""
        relative path to the build output directory
        (defaults to '%(default)s').
        """,
    )

    group = parser.add_argument_group("Build Options")
    group.add_argument(
        "--action",
        choices=BuildAction.LIST,
        default=BuildAction.DEFAULT,
        help="""
        cmake: execute CMake and exit.
        clean: delete existing build directory and exit.
        recmake: delete existing CMakeCache and execute CMake after that.
        build: execute MSBuild to Visual Studio solution files that created by cmake.
        rebuild: delete existing build directory and execute CMake and
        MSBuild after that.
        defaults to '%(default)s'.
        """,
    )

    group = parser.add_argument_group("CMake Options")
    group.add_argument(
        "--cmake-options",
        default=DEFAULT_CMAKE_OPTIONS_FILE,
        help="""
        path to the CMake options file. use "{key :value, ...}"
        to set specific parameters. defaults to %(default)s.
        """,
    )
    group.add_argument(
        "--build-type",
        choices=BuildType.LIST,
        default=BuildType.DEFAULT,
        help="defaults to %(default)s.",
    )
    group.add_argument(
        "--generator",
        help="""
        generator that passes to cmake.
        the default value decided by execution platform:
        (a) if executed at Windows and Visual Studio is installed in C: or D:
        drive, cmakew pass 'Visual Studio NN'  as a generator to cmake.
        (b) "Unix Makefiles" otherwise
        """,
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--debug",
        dest="log_level",
        action="store_const",
        const=logbook.DEBUG,
        default=logbook.INFO,
        help="for debug print.",
    )
    group.add_argument(
        "--quiet",
        dest="log_level",
        action="store_const",
        const=QUIET_LOG_LEVEL,
        default=logbook.INFO,
        help="suppress execution log messages.",
    )

    return parser.parse_args()

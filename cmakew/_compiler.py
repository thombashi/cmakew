#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import abc
import os.path
import re
import shutil

import six
import subprocrunner
import typepy

from ._logger import logger
from ._visual_studio import (
    find_vs_solution_file_list,
    vsinfo,
)


@six.add_metaclass(abc.ABCMeta)
class CompilerInterface(object):

    @abc.abstractmethod
    def build(self):
        pass

    @abc.abstractmethod
    def clean(self):
        pass


class AbstractCompiler(CompilerInterface):

    _VALIDATE_ERROR_MSG_TEMPLATE = (
        "build path must not a root directory path: actual={}")

    @property
    def build_dir_path(self):
        return self.__build_dir_path

    def __init__(self, build_dir_path):
        self._validate_build_dir_path(build_dir_path)
        self.__build_dir_path = os.path.abspath(
            os.path.expanduser(build_dir_path))

    def _validate_build_dir_path(self, dir_path):
        if typepy.is_null_string(dir_path):
            raise ValueError("build path must not a empty directory path")

        if dir_path == "/":
            raise ValueError(
                self._VALIDATE_ERROR_MSG_TEMPLATE.format(dir_path))

    def _run_build(self, build_command):
        runner = subprocrunner.SubprocessRunner(build_command)
        runner.run()

        if typepy.is_not_null_string(runner.stdout):
            logger.info(runner.stdout)

        if typepy.is_null_string(runner.stderr):
            return

        if runner.returncode == 0:
            logger.info(runner.stderr)
        else:
            logger.error(runner.stderr)

    def clean(self):
        self._validate_build_dir_path(self.build_dir_path)

        logger.debug('delete "{:s}" directory'.format(self.build_dir_path))
        shutil.rmtree(self.build_dir_path, ignore_errors=True)

        return 0


class WindowsCompiler(AbstractCompiler):
    def _validate_build_dir_path(self, dir_path):
        super(WindowsCompiler, self)._validate_build_dir_path(dir_path)

        if re.search(r"^[a-zA-Z]:\\?$", dir_path) is not None:
            raise ValueError(
                self._VALIDATE_ERROR_MSG_TEMPLATE.format(dir_path))

    def build(self):
        for solution_file in find_vs_solution_file_list(self.build_dir_path):
            self._run_build('"{:s}" {:s}'.format(
                vsinfo.msbuild_path, solution_file))


class LnuxCompiler(AbstractCompiler):
    def build(self):
        import multiprocessing

        try:
            make_command = "make -j{:d}".format(multiprocessing.cpu_count())
        except NotImplementedError:
            make_command = "make"

        self._run_build(make_command)


class CompilerFactory(object):
    @staticmethod
    def create(build_dir_path):
        import platform

        if platform.system() == "Windows":
            return WindowsCompiler(build_dir_path)

        return LnuxCompiler(build_dir_path)

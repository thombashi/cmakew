# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from collections import namedtuple
import itertools
import os.path
import platform
import re


def find_vs_solution_file_list(root_path):
    re_solution = re.compile("[\.]sln$")
    solution_file_path_list = []

    for filename in os.listdir(root_path):
        if re_solution.search(filename) is None:
            continue

        solution_file_path_list.append("/".join([root_path, filename]))

    return solution_file_path_list


class VisualStudioInfo(object):
    __RE_VS_DIR_NAME = re.compile("Microsoft Visual Studio [0-9]+[\.][0-9]+")
    __RE_VS_VERSION = re.compile("[0-9]+[\.][0-9]+")

    VersionInfo = namedtuple("VersionInfo", "major minor")

    @property
    def version_info(self):
        return self.__max_version_info

    @property
    def msbuild_path(self):
        return self.__msbuild_path

    def __init__(self, search_drive_list=["C:"]):
        self.__version_info_set = set()
        self.__max_version_info = None
        self.__msbuild_path = None

        if platform.system() != "Windows":
            return

        self.__program_files_dir_list = [
            "Program Files",
            "Program Files (x86)",
        ]

        self.__detect_version(search_drive_list)
        self.__detect_msbuild(search_drive_list)

    def __detect_version(self, search_drive_list):
        max_vs_version = 0

        for search_drive, program_files_dir in itertools.product(
                search_drive_list, self.__program_files_dir_list):

            try:
                dir_list = os.listdir(
                    "{:s}\\{:s}".format(search_drive, program_files_dir))
            except WindowsError:
                continue

            for dir_name in dir_list:
                match = self.__RE_VS_DIR_NAME.search(dir_name)
                if match is None:
                    continue

                version_string = self.__RE_VS_VERSION.search(
                    match.group()).group()
                vs_version = float(version_string)
                version_info = self.VersionInfo(*[
                    int(ver) for ver in version_string.split(".")])
                self.__version_info_set.add(version_info)

                if vs_version > max_vs_version:
                    max_vs_version = vs_version
                    self.__max_version_info = version_info

    def __detect_msbuild(self, search_drive_list):
        for search_drive, program_files_dir in itertools.product(
                search_drive_list, self.__program_files_dir_list):

            try:
                dir_list = os.listdir(
                    "{:s}\\{:s}".format(search_drive, program_files_dir))
            except WindowsError:
                continue

            for dir_name in dir_list:
                if dir_name != "MSBuild":
                    continue

                for version_info in reversed(sorted(self.__version_info_set)):
                    msbuild_path = "/".join([
                        search_drive,
                        program_files_dir,
                        dir_name,
                        "{:d}.{:d}".format(
                            version_info.major, version_info.minor),
                        "Bin",
                        "MSBuild.exe",
                    ])

                    if os.path.isfile(msbuild_path):
                        self.__msbuild_path = msbuild_path
                        return


vsinfo = VisualStudioInfo()

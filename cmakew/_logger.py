# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals

import logbook
import subprocrunner


logger = logbook.Logger("cmakew")
logger.disable()


def set_logger(is_enable):
    if is_enable != logger.disabled:
        # logger setting have not changed
        return

    if is_enable:
        logger.enable()
    else:
        logger.disable()

    subprocrunner.SubprocessRunner.default_error_log_level = logbook.DEBUG


def set_log_level(log_level):
    """
    Set logging level of this module. The module using
    `logbook <https://logbook.readthedocs.io/en/stable/>`__ module for logging.

    :param int log_level:
        One of the log level of the
        `logbook <https://logbook.readthedocs.io/en/stable/api/base.html>`__.
        Disabled logging if the ``log_level`` is ``logbook.NOTSET``.
    :raises LookupError: If ``log_level`` is an invalid value.
    """

    # validate log level
    logbook.get_level_name(log_level)

    if log_level == logger.level:
        return

    if log_level == logbook.NOTSET:
        set_logger(is_enable=False)
    else:
        set_logger(is_enable=True)

    logger.level = log_level
    subprocrunner.set_log_level(log_level)

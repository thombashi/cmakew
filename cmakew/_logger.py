# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import subprocrunner
import logbook


logger = logbook.Logger("cmakew")
logger.disable()


def set_logger(is_enable):
    if is_enable:
        logger.enable()
    else:
        logger.disable()


def set_log_level(log_level):
    """
    Set logging level of this module. The module using
    `logbook <http://logbook.readthedocs.io/en/stable/>`__ module for logging.

    :param int log_level:
        One of the log level of the
        `logbook <http://logbook.readthedocs.io/en/stable/api/base.html>`__.
        Disabled logging if the ``log_level`` is ``logbook.NOTSET``.
    """

    subprocrunner.set_log_level(log_level)

    if log_level == logbook.NOTSET:
        set_logger(is_enable=False)
    else:
        set_logger(is_enable=True)
        logger.level = log_level

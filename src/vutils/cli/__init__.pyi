#                                                         -*- coding: utf-8 -*-
# File:    ./src/vutils/cli/__init__.pyi
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2022-02-17 19:49:22 +0100
# Project: vutils-cli: Auxiliary library for writing CLI applications
#
# SPDX-License-Identifier: MIT
#

import pathlib
from typing import Callable, NoReturn, Protocol, TextIO

from typing_extensions import TypeAlias

from vutils.cli.errors import AppExitError
from vutils.cli.logging import LogFormatter

_ExcType: TypeAlias = type[Exception]

_ExitExcType: TypeAlias = type[AppExitError]
_ColorFuncType: TypeAlias = Callable[[str], str]

class _StreamsProtocol(Protocol):
    __output: TextIO
    __errout: TextIO

    def set_streams(
        self, ostream: TextIO | None, estream: TextIO | None
    ) -> None: ...
    def wout(self, text: str) -> None: ...
    def werr(self, text: str) -> None: ...

class _LoggerProtocol(Protocol):
    __logpath: pathlib.Path | None
    __formatter: LogFormatter
    __vlevel: int
    __dlevel: int

    def set_logger_props(
        self,
        logpath: pathlib.Path | None,
        formatter: LogFormatter | None,
        vlevel: int | None,
        dlevel: int | None,
    ) -> None: ...
    def set_log_style(self, name: str, color: _ColorFuncType) -> None: ...
    def wlog(self, msg: str) -> None: ...
    def linfo(self, msg: str, vlevel: int) -> None: ...
    def lwarn(self, msg: str) -> None: ...
    def lerror(self, msg: str) -> None: ...
    def ldebug(self, msg: str, dlevel: int) -> None: ...
    def __do_log(self, name: str, msg: str) -> None: ...

    # StreamsProxyMixin interface:
    def set_streams(
        self, ostream: TextIO | None, estream: TextIO | None
    ) -> None: ...
    def wout(self, text: str) -> None: ...
    def werr(self, text: str) -> None: ...

class _ApplicationProtocol(Protocol):
    EXIT_SUCCESS: int
    EXIT_FAILURE: int
    EXIT_EXCEPTION: _ExitExcType
    __elist: list[_ExcType]

    def catch(self, exc: _ExcType) -> None: ...
    def error(self, msg: str, ecode: int) -> NoReturn: ...
    def exit(self, ecode: int) -> NoReturn: ...
    def main(self, argv: list[str]) -> int: ...
    def run(self, argv: list[str]) -> int: ...
    def on_exit(self, ecode: int) -> None: ...
    def on_error(self, exc: Exception) -> int: ...

    # StreamsProxyMixin interface:
    def set_streams(
        self, ostream: TextIO | None, estream: TextIO | None
    ) -> None: ...
    def wout(self, text: str) -> None: ...
    def werr(self, text: str) -> None: ...

    # LoggerMixin interface:
    def set_logger_props(
        self,
        logpath: pathlib.Path | None,
        formatter: LogFormatter | None,
        vlevel: int | None,
        dlevel: int | None,
    ) -> None: ...
    def set_log_style(self, name: str, color: _ColorFuncType) -> None: ...
    def wlog(self, msg: str) -> None: ...
    def linfo(self, msg: str, vlevel: int) -> None: ...
    def lwarn(self, msg: str) -> None: ...
    def lerror(self, msg: str) -> None: ...
    def ldebug(self, msg: str, dlevel: int) -> None: ...
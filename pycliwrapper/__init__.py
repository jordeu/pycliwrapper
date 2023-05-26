import os
import subprocess
from typing import Iterable, Any


class CliWrapper:

    def __init__(self, command: str, parser=str, env=None):
        self._command = command
        self._parser = parser
        self._env = env

    def __getattr__(self, item):
        subcommand = item.replace('_', '-')
        return CliWrapper(f"{self._command} {subcommand}", parser=self._parser, env=self._env)

    def __call__(self, *args, **kwargs):
        arguments = self._parse_args(args)
        flags = self._parse_kwargs(kwargs)
        return CliWrapper(f"{self._command}{arguments}{flags}", parser=self._parser, env=self._env)

    def __invert__(self):
        env = self._env if self._env else os.environ
        out = subprocess.run([self._command], shell=True, text=True, check=True, env=env, stdout=subprocess.PIPE)
        return self._parser(out.stdout)

    def __dir__(self) -> Iterable[str]:
        return []

    def __str__(self):
        return self._command

    def __repr__(self):
        return self._command

    @staticmethod
    def _parse_args(args) -> str:
        if args is None or len(args) == 0:
            return ""
        return " " + " ".join((CliWrapper._parse_value(v) for v in args))

    @staticmethod
    def _parse_kwargs(kwargs) -> str:
        if kwargs is None or len(kwargs) == 0:
            return ""
        return " " + " ".join([CliWrapper._parse_option(k, v) for k, v in kwargs.items()])

    @staticmethod
    def _parse_option(key: str, value: Any) -> str:
        dash = "--" if len(key) > 1 else "-"
        if key.startswith("_"):
            dash = "-"
            key = key[1:]
        equal = "="
        if key.endswith("_"):
            equal = " "
            key = key[:-1]
        key = key.replace("_", "-")
        if isinstance(value, bool) and value:
            return f"{dash}{key}"
        quoted = CliWrapper._parse_value(value)
        return f"{dash}{key}{equal}{quoted}"

    @staticmethod
    def _parse_value(value: Any) -> str:
        return f"\"{value}\"" if isinstance(value, str) else str(value)









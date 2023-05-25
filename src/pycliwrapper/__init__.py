__version__ = "0.1"

import os
import subprocess


class CliWrapper:

    def __init__(self, command: str, parser=str, env=None):
        self._command = command
        self._parser = parser
        self._env = env

    def __getattr__(self, item):
        subcommand = item.replace('_', '-')
        return CliWrapper(f"{self._command} {subcommand}", parser=self._parser, env=self._env)

    def __call__(self, *args, **kwargs):
        arguments = " ".join(args)
        flags = " ".join([f"--{k}={v}" for k, v in kwargs.items()])
        return CliWrapper(f"{self._command} {arguments} {flags}", parser=self._parser, env=self._env)

    def __invert__(self):
        env = self._env if self._env else os.environ
        out = subprocess.run([self._command], shell=True, text=True, check=True, env=env, stdout=subprocess.PIPE)
        return self._parser(out.stdout)








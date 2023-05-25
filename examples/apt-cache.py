import sys
from subprocess import CalledProcessError

from pycliwrapper import CliWrapper


def run():
    apt_cache = CliWrapper("apt-cache", parser=lambda stdout: stdout.splitlines())
    res = ~apt_cache.search.bash
    print(res)

if __name__ == "__main__":
    try:
        run()
    except CalledProcessError as e:
        sys.exit(e.returncode)

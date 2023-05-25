import json
import sys
from subprocess import CalledProcessError

from pycliwrapper import CliWrapper


def run():
    tw = CliWrapper("tw -o json", parser=json.loads)

    res = ~tw.pipelines.list
    print("\nPIPELINES")
    print(res)

    res = ~tw.pipelines.list(filter="hello")
    print("\nHELLO PIPELINES")
    print(res)

    res = ~tw.compute_envs.list
    print("\nCOMPUTE ENVS")
    print(res)


if __name__ == "__main__":
    try:
        run()
    except CalledProcessError as e:
        sys.exit(e.returncode)

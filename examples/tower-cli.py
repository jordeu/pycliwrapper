import json
import sys
from subprocess import CalledProcessError

from pycliwrapper import CliWrapper


def run():
    # Build a wrapper on top of main command
    tw = CliWrapper("tw -o json", parser=json.loads)

    # Build the command that you want to execute
    # using Python syntax. A dot means a subcommand and
    # flags are pass as normal python variables.
    print("PIPELINES")
    cmd = tw.pipelines.list(filter="hello")

    # You can see the actual command that will be run
    # >> tw -o json pipelines list --filter="hello"
    print(f"Executing: {cmd}")

    # Execute it using the ~ operator and automatically
    # parse the output with the given parser
    print(~cmd)

    # Build and execute the command in one line
    # >> tw -o json compute-envs list
    print("\nCOMPUTE ENVS")
    print(~tw.compute_envs.list)

    # Mixing positional and flag arguments
    # >> tw -o json launch nf-core-nanoseq --workspace="community/showcase"
    print("\nLAUNCH")
    print(~tw.launch("nf-core-nanoseq", workspace="community/showcase"))

    # More complex example
    # >> tw -o json runs view -i 2gHGbjH9fRDuaW task -t=1 --execution-time
    print("\nVIEW")
    print(~tw.runs.view(i="2gHGbjH9fRDuaW").task(t=1, execution_time=True))


if __name__ == "__main__":
    try:
        run()
    except CalledProcessError as e:
        # On case of error CalledProcessError is raised
        sys.exit(e.returncode)

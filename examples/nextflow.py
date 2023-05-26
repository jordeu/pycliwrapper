import sys
from subprocess import CalledProcessError

from pycliwrapper import CliWrapper


def run():
    # Build a wrapper on top of main command
    nextflow = CliWrapper("nextflow")

    # Hello world
    # >> nextflow run "nextflow-io/hello"
    print(~nextflow.run("nextflow-io/hello"))

    # Mixing Nextflow options and pipeline options
    # >> nextflow run "nf-core/rnaseq" -profile "docker,test" -r "3.10.1" --outdir="./results"
    # TIP: the _ at the beginning means that you want to use a "-" instead of a "--" even if the key has more than one character
    # TIP: the _ at the end means that you want to use a " " instead of a "=" even if the key has more than one character
    print(~nextflow.run("nf-core/rnaseq", _profile_="docker,test", _r_="3.10.1", outdir="./results"))


if __name__ == "__main__":
    try:
        run()
    except CalledProcessError as e:
        # On case of error CalledProcessError is raised
        sys.exit(e.returncode)
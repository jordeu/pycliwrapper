# Generic Python CLI Wrapper

Wrap any CLI tool to Python like syntax.

## Quick start

```python
from pycliwrapper import CliWrapper
apt_cache = CliWrapper("apt-cache", parser=lambda stdout: stdout.splitlines())

# Equivalent to run: "apt-cache search bash" and parsing
# the output as a list
res = ~apt_cache.search.bash
print(res)
```

## Parsing output as JSON

```python
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
print(~tw.compute_envs.list)

# Mixing positional and flag arguments
# >> tw -o json launch nf-core-nanoseq --workspace="community/showcase"
print(~tw.launch("nf-core-nanoseq", workspace="community/showcase"))

# More complex example
# >> tw -o json runs view -i 2gHGbjH9fRDuaW task -t=1 --execution-time
print(~tw.runs.view(i="2gHGbjH9fRDuaW").task(t=1, execution_time=True))
```

## Non standard CLI support

```python
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
```
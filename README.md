# Generic Python CLI Wrapper

Wrap any CLI tool to Python like syntax.

## Usage example

```
from pycliwrapper import CliWrapper
apt_cache = CliWrapper("apt-cache", parser=lambda stdout: stdout.splitlines())

# Equivalent to run: "apt-cache search bash" 
res = ~apt_cache.search.bash
print(res)
```
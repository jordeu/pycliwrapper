# Generic Python CLI Wrapper

Proof of concept class to automatically wrap any CLI to Python like syntax.

## Usage example

```
from pycliwrapper import CliWrapper
apt_cache = CliWrapper("apt-cache", parser=lambda stdout: stdout.splitlines())
res = ~apt_cache.search.bash
print(res)
```
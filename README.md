# Title

## Setup

1. Install micropython on raspberry pi
2. Setup virtual environment for python and install requirements
3. Use rshell to do the rest
4. Install packages using mip
5. Create config.py based on example-config.py

## Setup Virtual Environment

```bash
# Setup venv
python3 -m venv venv
source venv/bin/activate
# Install requirements
pip install -r requirements.txt
```

## shell

```bash
rshell
rshell ls
rshell
# ctrl-x seems to close repl
ls /pyboard

rshell repl
# sync src with pyboard
rshell rsync src /pyboard

# run specific file in repl
exec(open('file.py').read())
```

## Install Packages

```bash
# Install mip packages
rshell
repl
import mip
mip.install('umqtt.simple')
```

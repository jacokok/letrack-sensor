# Title

```bash
wezterm serial --baud 115200 /dev/ttyUSB0
```

```bash
# Install Subs
pip install -U micropython-esp8266-stubs --no-user
```

```bash
# Install mip packages
import mip
mip.install('umqtt.simple')
```

## Configure VsCode

```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticSeverityOverrides": {
    "reportMissingModuleSource": "none"
  },
  "python.analysis.typeshedPaths": [".venv/Lib/site-packages"]
}
```

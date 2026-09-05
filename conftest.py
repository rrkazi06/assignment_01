"""Make the module in code/ importable from the tests (e.g. `import bill`)."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "code"))

# checks for various run time environments are in place.
# Very limited checks.

import pymc as pm
import arviz as az
import numpy as np

# make certain that preliZ and arviZ versions are correct.
np.random.seed(0)
print(pm.__version__, az.__version__)

# determine if the correct python environment is in place.
import sys
print("Python executable:", sys.executable)


# setting up ROOT shortcut for paths in code
import pathlib

ROOT = pathlib.Path(".").resolve()
FIG_DIR = ROOT / "fig"
# test that ROOT works as expected.
FIG_DIR.mkdir(exist_ok=True)


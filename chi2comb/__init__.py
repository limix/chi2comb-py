"""
Combination of chi-squared distributions
========================================

Functions
---------
chi2comb_cdf  Function distribution of combination of chi-squared distributions.

Documentation can be found at <https://github.com/limix/chi2comb-py>.
"""

from __future__ import absolute_import

try:
    from ._ffi import ffi as _
except Exception as e:
    msg = "\nIt is likely caused by a broken installation of this package."
    msg += "\nPlease, make sure you have a C compiler and try to uninstall"
    msg += "\nand reinstall the package again."
    e.msg = e.msg + msg
    raise e

from ._chi2comb import chi2comb_cdf, ChiSquared, Info
from ._testit import test

__version__ = "0.0.1"

__all__ = ["__version__", "test", "chi2comb_cdf", "ChiSquared", "Info"]

"""
Combination of chi-squared distributions
========================================

This package estimates cumulative density functions of linear combinations of
independent noncentral χ² random variables and a standard Normal distribution.
Formally, it estimates P[Q<q], where::

    Q = λ₁X₁ + ... + λₙXₙ + σX₀.

Xᵢ (𝚒≠𝟶) is an independent random variable following a noncentral χ² distribution with
nᵢ degrees of freedom and noncentrality parameter λᵢ.
X₀ is an independent random variable having a standard Normal distribution.

Function
--------
chi2comb_cdf  Function distribution of combination of χ² distributions.

Classes
-------
ChiSquared    Noncentral χ² distribution.
Info          Algorithm information.

Usage
-----
Consider the following linear combination of four random variables::

    Q = 6⋅X₁ + 3⋅X₂ + 1⋅X₃ + 2⋅X₀,

where X₁, X₂, and X₃ are noncentral χ² random variables having degrees of freedom
n₁=n₂=1 and n₃=2 and noncentrality parameters λ₁=0.5 and λ₂=λ₃=0.
Let us estimate P[Q<1]::

    >>> from chi2comb import chi2comb_cdf, ChiSquared
    >>>
    >>> gcoef = 2
    >>> ncents = [0.5, 0, 0]
    >>> q = 1
    >>> dofs = [1, 1, 2]
    >>> coefs = [6, 3, 1]
    >>> chi2s = [ChiSquared(coefs[i], ncents[i], dofs[i]) for i in range(3)]
    >>> result, errno, info = chi2comb_cdf(q, chi2s, gcoef)
    >>> result  # doctest: +FLOAT_CMP
    0.050870657088644244
    >>> errno
    0
    >>> info  # doctest: +FLOAT_CMP
    Info(emag=0.6430413191446991, niterms=43, nints=1, intv=0.03462571527167856, truc=1.4608856930426104, sd=0.0, ncycles=21)

The estimated value is P[Q<1] ≈ 0.0587.
"""
try:
    from ._ffi import ffi

    del ffi
except Exception as e:
    _ffi_err = """
It is likely caused by a broken installation of this package.
Please, make sure you have a C compiler and try to uninstall
and reinstall the package again."""

    raise RuntimeError(str(e) + _ffi_err)

from ._chi2comb import ChiSquared, Info, chi2comb_cdf
from ._testit import test

__version__ = "0.1.0"

__all__ = ["__version__", "test", "chi2comb_cdf", "ChiSquared", "Info"]

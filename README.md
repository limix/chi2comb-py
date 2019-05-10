# chi2comb

[![Travis](https://img.shields.io/travis/com/limix/chi2comb-py.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.com/limix/chi2comb-py) [![AppVeyor](https://img.shields.io/appveyor/ci/Horta/chi2comb-py.svg?style=flat-square&label=windows%20build)](https://ci.appveyor.com/project/Horta/chi2comb-py)

This package estimates cumulative density functions of linear combinations of
independent noncentral χ² random variables and a standard Normal distribution.
Formally, it estimates P[Q<q], where:

    Q = λ₁X₁ + ... + λₙXₙ + σX₀.

Xᵢ (𝚒≠𝟶) is an independent random variable following a noncentral χ² distribution with
nᵢ degrees of freedom and noncentrality parameter λᵢ.
X₀ is an independent random variable having a standard Normal distribution.

## Install

It can be installed using the pip command

```bash
pip install chi2comb
```

## Usage


Consider the following linear combination of four random variables:

    Q = 6⋅X₁ + 3⋅X₂ + 1⋅X₃ + 2⋅X₀,

where X₁, X₂, and X₃ are noncentral χ² random variables having degrees of freedom
n₁=n₂=1 and n₃=2 and noncentrality parameters λ₁=0.5 and λ₂=λ₃=0.
Let us estimate P[Q<1]:

```python
>>> from chi2comb import chi2comb_cdf, ChiSquared
>>>
>>> gcoef = 2
>>> ncents = [0.5, 0, 0]
>>> q = 1
>>> dofs = [1, 1, 2]
>>> coefs = [6, 3, 1]
>>> chi2s = [ChiSquared(coefs[i], ncents[i], dofs[i]) for i in range(3)]
>>> result, errno, info = chi2comb_cdf(q, chi2s, gcoef)
>>> result
0.050870657088644244
>>> errno
0
>>> info
Info(emag=0.6430413191446991, niterms=43, nints=1, intv=0.03462571527167856, truc=1.4608856930426104, sd=0.0, ncycles=21)
```

The estimated value is P[Q<1] ≈ 0.0587.

## Problems

If you encounter any issue, please, [submit it](https://github.com/limix/chi2comb-py/issues/new).

## Authors

* [Danilo Horta](https://github.com/horta)

## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/limix/chi2comb-py/master/LICENSE.md).

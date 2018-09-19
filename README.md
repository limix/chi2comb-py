# chi2comb

[![Travis](https://img.shields.io/travis/limix/chi2comb-py.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.org/limix/chi2comb-py) [![AppVeyor](https://img.shields.io/appveyor/ci/Horta/chi2comb-py.svg?style=flat-square&label=windows%20build)](https://ci.appveyor.com/project/Horta/chi2comb-py)

## Install

The recommended way to install this package is via [conda](https://conda.io/docs/)

```bash
conda install -c conda-forge chi2comb
```

Alternatively, it can be installed using the pip command

```bash
pip install chi2comb
```

## Usage

```python
>>> from chi2comb import chi2comb_cdf, ChiSquared
>>>
>>> gcoef = 0.0
>>> ncents = [0, 0, 0]
>>> q = 1
>>> dofs = [1, 1, 1]
>>> coefs = [6, 3, 1]
>>> chi2s = [ChiSquared(coefs[i], ncents[i], dofs[i]) for i in range(3)]
>>> result, errno, info = chi2comb_cdf(q, chi2s, gcoef)
>>> result
0.054212946675253226
>>> errno
0
>>> info
Info(emag=0.7623482489861554, niterms=744, nints=2, intv=0.03819311576613404, truc=53.37968999861114, sd=0.0, ncycles=51)
```

## Problems

If you encounter any issue, please, [submit it](https://github.com/limix/chi2comb-py/issues/new).

## Authors

* [Danilo Horta](https://github.com/horta)

## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/limix/chi2comb-py/master/LICENSE.md).

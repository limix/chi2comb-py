from numpy import asarray
from ._ffi import ffi
from ._ffi.lib import chi2comb_cdf as c_chi2comb_cdf


class ChiSquared(object):
    def __init__(self, coef, ncent, dof):
        self.coef = float(coef)
        self.ncent = float(ncent)
        self.dof = int(dof)


class Info(object):
    def __init__(self):
        self.emag = 0.0
        self.niterms = 0
        self.nints = 0
        self.intv = 0.0
        self.truc = 0.0
        self.sd = 0.0
        self.ncycles = 0
    

def chi2comb_cdf(q, chi2s, gcoef, lim=1000, atol=1e-9):
    q = float(q)
    c_chi2s = ffi.new("struct chi2comb_chisquareds *")
    c_info = ffi.new("struct chi2comb_info *")

    ncents = asarray([float(i.ncent) for i in chi2s])
    coefs = asarray([float(i.coef) for i in chi2s])
    dofs = asarray([int(i.dof) for i in chi2s], "int{}".format(ffi.sizeof("int") * 8))

    c_chi2s.ncents = ffi.cast("double *", ncents.ctypes.data)
    c_chi2s.coefs = ffi.cast("double *", coefs.ctypes.data)
    c_chi2s.dofs = ffi.cast("int *", dofs.ctypes.data)
    c_chi2s.n = len(chi2s)

    result = ffi.new("double *")
    errno = c_chi2comb_cdf(q, c_chi2s, gcoef, lim, atol, c_info, result)

    info = Info()
    methods = ["emag", "niterms", "nints", "intv", "truc", "sd", "ncycles"]
    for i in methods:
        setattr(info, i, getattr(c_info, i))

    return (result[0], errno, info)

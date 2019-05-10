from array import array

from ._ffi import ffi
from ._ffi.lib import chi2comb_cdf as c_chi2comb_cdf


class ChiSquared(object):
    """
    Noncentral χ² distribution.
    """

    def __init__(self, coef, ncent, dof):
        self.coef = float(coef)
        self.ncent = float(ncent)
        self.dof = int(dof)

    def __repr__(self):
        msg = "(coef={}, ncent={}, dof={})".format(self.coef, self.ncent, self.dof)
        return "ChiSquared" + msg


class Info(object):
    """
    Algorithm information.
    """

    def __init__(self):
        self.emag = 0.0
        self.niterms = 0
        self.nints = 0
        self.intv = 0.0
        self.truc = 0.0
        self.sd = 0.0
        self.ncycles = 0

    def __repr__(self):
        msg = "(emag={}, niterms={}, ".format(self.emag, self.niterms)
        msg += "nints={}, ".format(self.nints)
        msg += "intv={}, truc={}, sd={}".format(self.intv, self.truc, self.sd)
        msg += ", ncycles={})".format(self.ncycles)
        return "Info" + msg


def chi2comb_cdf(q, chi2s, gcoef, lim=1000, atol=1e-4):
    """
    Function distribution of combination of noncentral chi-squared distributions.

    Parameters
    ----------
    q : float
        Value point at which distribution function is to be evaluated.
    chi2s : list
        List of ChiSquared objects defining noncentral χ² distributions.
    gcoef : float
        Coefficient of the standard Normal distribution.
    lim : int, optional
        Maximum number of integration terms. It defaults to ``1000``.
    atol : float, optional
        Absolute error tolerance. It defaults to ``1e-4``.

    Returns
    -------
    result : float
        Estimated c.d.f. evaluated at ``q``.
    error : int
        0: completed successfully
        1: required accuracy not achieved
        2: round-off error possibly significant
        3: invalid parameters
        4: unable to locate integration parameters
        5: out of memory
    info : Info
        Algorithm information.
    """

    int_type = "i"
    if array(int_type, [0]).itemsize != ffi.sizeof("int"):
        int_type = "l"
        if array(int_type, [0]).itemsize != ffi.sizeof("int"):
            raise RuntimeError("Could not infer a proper integer representation.")

    if array("d", [0.0]).itemsize != ffi.sizeof("double"):
        raise RuntimeError("Could not infer a proper double representation.")

    q = float(q)
    c_chi2s = ffi.new("struct chi2comb_chisquareds *")
    c_info = ffi.new("struct chi2comb_info *")

    ncents = array("d", [float(i.ncent) for i in chi2s])
    coefs = array("d", [float(i.coef) for i in chi2s])
    dofs = array(int_type, [int(i.dof) for i in chi2s])

    c_chi2s.ncents = ffi.cast("double *", ncents.buffer_info()[0])
    c_chi2s.coefs = ffi.cast("double *", coefs.buffer_info()[0])
    c_chi2s.dofs = ffi.cast("int *", dofs.buffer_info()[0])
    c_chi2s.n = len(chi2s)

    result = ffi.new("double *")
    errno = c_chi2comb_cdf(q, c_chi2s, gcoef, lim, atol, c_info, result)

    info = Info()
    methods = ["emag", "niterms", "nints", "intv", "truc", "sd", "ncycles"]
    for i in methods:
        setattr(info, i, getattr(c_info, i))

    return (result[0], errno, info)

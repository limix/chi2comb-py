from chi2comb import chi2comb_cdf, ChiSquared


def test_chi2comb():
    expected = 0.054212946675253226303
    gcoef = 0.0
    ncents = [0, 0, 0]
    q = 1
    dofs = [1, 1, 1]
    coefs = [6, 3, 1]

    chi2s = [ChiSquared(coefs[i], ncents[i], dofs[i]) for i in range(3)]
    result, errno, info = chi2comb_cdf(q, chi2s, gcoef, atol=1e-4)
    assert abs(result - expected) < 1e-7

    expected = 0.96037034711779101226
    qcoef = 0.0
    ncents = [6, 2, 6, 2]
    q = 140
    dofs = [6, 2, 1, 1]
    coefs = [7, 3, -7, -3]

    chi2s = [ChiSquared(coefs[i], ncents[i], dofs[i]) for i in range(4)]
    result, errno, info = chi2comb_cdf(q, chi2s, qcoef, atol=1e-4)
    assert abs(result - expected) < 1e-7

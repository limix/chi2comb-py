struct chi2comb_chisquareds {
  const double *coefs;
  const double *ncents;
  const int *dofs;
  int n;
};

struct chi2comb_info {
  double emag;
  int niterms;
  int nints;
  double intv;
  double truc;
  double sd;
  int ncycles;
};

int chi2comb_cdf(double q, struct chi2comb_chisquareds *chi2s, double gcoef,
                 int lim, double abstol, struct chi2comb_info *info,
                 double *result);
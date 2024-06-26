class PrefixAverage {

  public static double[] prefixAverage1(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    for (int j = 0; j < n; j++) {
      double total = 0;
      for (int i = 0; i <= j; i++)
        total += x[i];
      a[j] = total / (j + 1);
    }
    return a;
  }

  public static double[] prefixAverage2(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    double total = 0;
    for (int j = 0; j < n; j++) {
      total += x[j];
      a[j] = total / (j + 1);
    }
    return a;
  }
}

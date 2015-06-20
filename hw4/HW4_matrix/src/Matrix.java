public class Matrix {
    public static double[][] times(double[][] a, double[][] b) {
        // Write code to calculate C = A * B.
        int i, j, k;

        int n = a.length;
        int n2 = b.length;

        if (n*n2 == 0) {
            throw new IllegalArgumentException("Do not put empty arrays.");
        }

        int n3 = a[0].length;
        int n4 = b[0].length;
        if (n != n2 || n2 != n3 || n3 != n4) {
            throw new IllegalArgumentException("Please put two same size N*N matrixs.");
        }

        double[][] c = new double[n][n];

        for (i = 0; i < n; i++) {
            for (k = 0; k < n; k++) {
                for (j = 0; j < n; j++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;

    }
}

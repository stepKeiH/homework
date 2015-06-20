import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class MatrixTest {
    private final static double EPS = 1e-10;

    @Test
    public void test1() throws Exception {
        // Testing simplest case.
        double[][] a = {{1.1}}, b = {{1.1}};
        double[][] c = Matrix.times(a, b);
        assertEquals(c[0][0], 1.21, EPS);
    }

    @Test
    public void test2() throws Exception {
        // Testing fractional case.
        double[][] a = {{1.3}}, b = {{1.1}};
        double[][] c = Matrix.times(a, b);
        assertEquals(c[0][0], 1.43, EPS);
    }

    @Test
    public void test3() throws Exception {
        // Testing minus values.
        double[][] a = {{-1,3},{0,2}}, b = {{-4,5},{-1,1}}, c = {{1,-2},{-2,2}};
        assertArrayEquals(c, Matrix.times(a, b));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test4() throws Exception {
        // Testing empty matrix.
        double[][] a = {{}}, b = {{-4,5},{-1,1}};
        Matrix.times(a, b);
    }

    @Test(expected = IllegalArgumentException.class)
    public void test5() throws Exception {
        // Testing not N*N matrix.
        double[][] a = {{-1,3},{0,2},{4,5}}, b = {{-4,5},{-1,1}};
        Matrix.times(a, b);
    }
} 

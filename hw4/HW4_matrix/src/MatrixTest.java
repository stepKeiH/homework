import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class MatrixTest {
    @Test
    public void test1() throws Exception {
        // Testing simplest case
        double[][] a = {{1.0}}, b = {{1.0}}, c = {{1.0}};
        assertArrayEquals(c, Matrix.times(a, b));
    }

    @Test
    public void test2() throws Exception {
        // Testing minus values.
        double[][] a = {{-1,3},{0,2}}, b = {{-4,5},{-1,1}}, c = {{1,-2},{-2,2}};
        assertArrayEquals(c, Matrix.times(a, b));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test3() throws Exception {
        // Testing empty matrix.
        double[][] a = {{}}, b = {{-4,5},{-1,1}};
        Matrix.times(a, b);
    }

    @Test(expected = IllegalArgumentException.class)
    public void test4() throws Exception {
        // Testing not N*N matrix.
        double[][] a = {{-1,3},{0,2},{4,5}}, b = {{-4,5},{-1,1}};
        Matrix.times(a, b);
    }
} 

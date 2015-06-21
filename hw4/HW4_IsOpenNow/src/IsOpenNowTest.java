import org.junit.Test;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class IsOpenNowTest {
    private static final String filename = "IsOpenNow.txt";

    @Test
    public void test1() throws Exception {
        // Testing true case.
        IsOpenNow a = new IsOpenNow(filename);
        assertTrue(a.isOpenNow("Sun", 0, 0));
        assertTrue(a.isOpenNow("Sun", 24, 0));
        assertTrue(a.isOpenNow("Mon", 12, 0));
        assertTrue(a.isOpenNow("Fri", 24, 0));
    }

    @Test
    public void test2() throws Exception {
        // Testing false case.
        IsOpenNow a = new IsOpenNow(filename);
        assertFalse(a.isOpenNow("Tue", 15, 0));
        assertFalse(a.isOpenNow("Wed", 16, 0));
        assertFalse(a.isOpenNow("Thu", 2, 15));
        assertFalse(a.isOpenNow("Sat", 0, 0));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test3() throws Exception {
        // Testing invalid inputs.
        IsOpenNow a = new IsOpenNow(filename);
        a.isOpenNow("Tue", 25, 0);
        a.isOpenNow("Wed", 16, 75);
        a.isOpenNow("The", 2, 0);
        a.isOpenNow("Sun", 24, 15);
    }
}

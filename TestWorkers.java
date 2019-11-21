package Test;

import java.util.concurrent.CountDownLatch;
import java.util.stream.IntStream;

public class TestWorkers {
    private static Integer var = 0;

    private static synchronized void incrementVar(int a){
        var++;
    }
    public static void main(String[] args) {
        final CountDownLatch counter = new CountDownLatch(2);

        final Runnable runnable = () -> {
            IntStream.range(0, 10).forEach(m -> incrementVar(m));
            counter.countDown();
        };
        new Thread(runnable).start();
        new Thread(runnable).start();
        try {
            counter.await();
            System.out.println(var);
        } catch (InterruptedException e) {
// ignored
        }
    }
}
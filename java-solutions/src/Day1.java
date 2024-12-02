import java.io.File;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Scanner;

public class Day1 {
    private static String INPUT_FILE = "../inputs/1.input";
    public static void main(String[] args) throws Exception {
        long start1 = 0, 
            end1 = 0, 
            start2 = 0, 
            end2 = 0;

        start1 = System.nanoTime();
        part1();
        end1 = System.nanoTime();
        start2 = System.nanoTime();
        part2();
        end2 = System.nanoTime();

        System.out.printf("\n\nPart 1 took %dms to run", Math.round((end1 - start1) / 1000000.0));
        System.out.printf("\nPart 2 took %dms to run", Math.round((end2 - start2) / 1000000.0));
    }

    private static void part1() throws Exception {
        Scanner in = new Scanner(new File(INPUT_FILE));
        ArrayList<Integer> left = new ArrayList<>();
        ArrayList<Integer> right = new ArrayList<>();

        while (in.hasNext()) {
            left.add(in.nextInt());
            right.add(in.nextInt());
        }

        left.sort(Comparator.naturalOrder());
        right.sort(Comparator.naturalOrder());

        int totalDiff = 0;
        for (int i = 0; i < left.size(); i++) {
            totalDiff += Math.abs(left.get(i) - right.get(i));
        }
        in.close();

        System.out.printf("Part 1: %d\n", totalDiff);
    }

    private static void part2() throws Exception {
        Scanner in = new Scanner(new File(INPUT_FILE));
        HashMap<Integer, Integer> leftNumCounts = new HashMap<>();
        HashMap<Integer, Integer> rightNumCounts = new HashMap<>();
        while (in.hasNext()) {
            Integer leftNum = in.nextInt();
            Integer rightNum = in.nextInt();
            leftNumCounts.put(leftNum, leftNumCounts.getOrDefault(leftNum, 0) + 1);
            rightNumCounts.put(rightNum, rightNumCounts.getOrDefault(rightNum, 0) + 1);
        }
        in.close();

        int simScore = 0;
        for (Integer num: leftNumCounts.keySet()) {
            simScore += num * rightNumCounts.getOrDefault(num, 0) * leftNumCounts.get(num);
        }
        System.out.printf("Part 2: %d\n", simScore);
    }
}
import java.io.*;
import java.util.*;

public class BearSortsDiv2 {
	public double getProbability(int[] seq) {
		return 0.0;
	}

// CUT begin
	public static void main(String[] args){
		System.err.println("BearSortsDiv2 (1000 Points)");
		System.err.println();
		HashSet<Integer> cases = new HashSet<Integer>();
        for (int i = 0; i < args.length; ++i) cases.add(Integer.parseInt(args[i]));
        runTest(cases);
	}

	static void runTest(HashSet<Integer> caseSet) {
	    int cases = 0, passed = 0;
	    while (true) {
	    	String label = Reader.nextLine();
	    	if (label == null || !label.startsWith("--"))
	    		break;

            int[] seq = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < seq.length; ++i)
                seq[i] = Integer.parseInt(Reader.nextLine());
            Reader.nextLine();
            double __answer = Double.parseDouble(Reader.nextLine());

            cases++;
            if (caseSet.size() > 0 && !caseSet.contains(cases - 1))
                continue;
    		System.err.print(String.format("  Testcase #%d ... ", cases - 1));

            if (doTest(seq, __answer))
                passed++;
	    }
	    if (caseSet.size() > 0) cases = caseSet.size();
        System.err.println(String.format("%nPassed : %d/%d cases", passed, cases));

        int T = (int)(System.currentTimeMillis() / 1000) - 1438446354;
        double PT = T / 60.0, TT = 75.0;
        System.err.println(String.format("Time   : %d minutes %d secs%nScore  : %.2f points", T / 60, T % 60, 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))));
	}

	static boolean doTest(int[] seq, double __expected) {
		long startTime = System.currentTimeMillis();
		Throwable exception = null;
		BearSortsDiv2 instance = new BearSortsDiv2();
		double __result = 0.0;
		try {
			__result = instance.getProbability(seq);
		}
		catch (Throwable e) { exception = e; }
		double elapsed = (System.currentTimeMillis() - startTime) / 1000.0;

		if (exception != null) {
			System.err.println("RUNTIME ERROR!");
			exception.printStackTrace();
			return false;
		}
		else if (doubleEquals(__expected, __result)) {
			System.err.println("PASSED! " + String.format("(%.2f seconds)", elapsed));
			return true;
		}
		else {
			System.err.println("FAILED! " + String.format("(%.2f seconds)", elapsed));
			System.err.println("           Expected: " + __expected);
			System.err.println("           Received: " + __result);
			return false;
		}
	}

	static boolean doubleEquals(double a, double b) {
	    return !Double.isNaN(a) && !Double.isNaN(b) && Math.abs(b - a) <= 1e-9 * Math.max(1.0, Math.abs(a) );
	}

	static class Reader {
        private static final String dataFileName = "BearSortsDiv2.sample";
	    private static BufferedReader reader;

	    public static String nextLine() {
	        try {
                if (reader == null) {
                    reader = new BufferedReader(new InputStreamReader(new FileInputStream(dataFileName)));
                }
                return reader.readLine();
	        }
	        catch (IOException e) {
	            System.err.println("FATAL!! IOException");
	            e.printStackTrace();
	            System.exit(1);
	        }
	        return "";
	    }
	}
// CUT end
}

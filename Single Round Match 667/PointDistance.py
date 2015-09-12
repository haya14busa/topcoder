# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

class PointDistance:
    def findPoint(self, x1, y1, x2, y2):
        a = (x1, y1)
        b = (x2, y2)
        assert -50 <= x1 <= 50
        assert (x1, y1) != (x2, y2)
        if x1 > x2:
            return (x2 - 1, y2)
        elif x1 == x2:
            if y1 < y2:
                return (x2, y2 + 1)
            else:
                return (x2, y2 - 1)
        else:
            assert x1 < x2
            return (x2 + 1, y2)

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(x1, y1, x2, y2, __expected):
    startTime = time.time()
    instance = PointDistance()
    exception = None
    try:
        __result = instance.findPoint(x1, y1, x2, y2);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("PointDistance (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PointDistance.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x1 = int(f.readline().rstrip())
            y1 = int(f.readline().rstrip())
            x2 = int(f.readline().rstrip())
            y2 = int(f.readline().rstrip())
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x1, y1, x2, y2, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1441983611
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end

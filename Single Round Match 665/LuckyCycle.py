# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Node():
    def __init__(self, nid):  # node id
        self.nid = nid
        self.to = None
        self.to_w = None
        self.from_ = None
        self.from_w = None

    def __repr__(self):
        return 'Node(' + str(self.nid) + ')'

    def connect(self, that, weight):
        self.to = that
        that.from_ = self
        self.to_w = weight
        that.from_w = weight

        

class LuckyCycle:
    def getEdge(self, edge1, edge2, weight):
        n = len(edge1) + 1
        assert 2 <= n <= 100
        nodes = list(map(lambda i: Node(i), range(1, n + 1)))
        assert len(nodes) == n
        for i in range(n - 1):
            f = edge1[i]
            t = edge2[i]
            nodes[f - 1].connect(nodes[t - 1], weight[i])

        # print('')
        # print('-' * 10)
        # for i in range(n - 1):
            # print(nodes[i].to, nodes[i].to_w)
        for node in nodes:
            ws = 0  # 4 -> -1, 7 -> +1
            el = 0  # edge length
            start_node = node
            while node.to:
                ws += (1 if node.to_w == 7 else -1)
                el += 1
                if el % 2 and abs(ws) == 1 and el > 1:
                    return [start_node.nid, node.nid, 4 if ws > 0 else 7]
                    # bnode = node
                    # while bnode.from_:
                    #     bnode = bnode.from_
                    #     pass
                        
                node = node.to
            
        return []

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

def do_test(edge1, edge2, weight, __expected):
    startTime = time.time()
    instance = LuckyCycle()
    exception = None
    try:
        __result = instance.getEdge(edge1, edge2, weight);
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
    sys.stdout.write("LuckyCycle (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LuckyCycle.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            edge1 = []
            for i in range(0, int(f.readline())):
                edge1.append(int(f.readline().rstrip()))
            edge1 = tuple(edge1)
            edge2 = []
            for i in range(0, int(f.readline())):
                edge2.append(int(f.readline().rstrip()))
            edge2 = tuple(edge2)
            weight = []
            for i in range(0, int(f.readline())):
                weight.append(int(f.readline().rstrip()))
            weight = tuple(weight)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(edge1, edge2, weight, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1439292894
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end

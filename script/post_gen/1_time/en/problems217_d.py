Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx + 1] - cuts[idx - 1])

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        elif c == 2:
            cuts.sort()
            for j in range(len(cuts)):
                if cuts[j] == x:
                    print(cuts[j + 1] - cuts[j])
                    break

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
            cut.sort()
        else:
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i+1] - cut[i])
                    break

=======
Suggestion 4

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
            cut.sort()
        else:
            print(cut[cut.index(x) + 1] - cut[cut.index(x)])

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    cut = [0] * (L + 1)
    cut[0] = 1
    cut[L] = 1
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut[x] = 1
        else:
            ans = 0
            for i in range(x, L + 1):
                if cut[i] == 1:
                    ans = i - x
                    break
            print(ans)

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    #L = 5
    #Q = 3
    #c = [2, 1, 2]
    #x = [2, 3, 2]
    c = []
    x = []
    for i in range(Q):
        c_i, x_i = map(int, input().split())
        c.append(c_i)
        x.append(x_i)
    #print(c)
    #print(x)
    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =", x)
    #print("")
    #print("")

    #print("L =", L)
    #print("Q =", Q)
    #print("c =", c)
    #print("x =",

=======
Suggestion 7

def main():
    L, Q = map(int, input().split())
    #print(L, Q)
    cut = [0] * (L + 1)
    cut[0] = 1
    cut[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut[x] = 1
        if c == 2:
            #print(cut)
            for j in range(x, -1, -1):
                if cut[j] == 1:
                    x1 = j
                    break
            for j in range(x, L + 1):
                if cut[j] == 1:
                    x2 = j
                    break
            print(x2 - x1)

=======
Suggestion 8

def main():
    import sys
    from bisect import bisect_left
    from collections import deque
    input = sys.stdin.readline
    L,Q = map(int,input().split())
    L = L
    Q = Q
    d = deque()
    d.append(0)
    d.append(L)
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            d.append(x)
            d = deque(sorted(d))
        if c == 2:
            idx = bisect_left(d,x)
            print(d[idx]-d[idx-1])

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    #print(L, Q)
    #print("

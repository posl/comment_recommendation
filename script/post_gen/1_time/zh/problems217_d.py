Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    cuts = []
    for i in range(Q):
        cuts.append(list(map(int, input().split())))
    cuts.sort(key=lambda x: x[0])
    cuts.sort(key=lambda x: x[1])
    print(cuts)
    for i in range(Q):
        if cuts[i][0] == 1:
            cuts[i][0] = 0
        else:
            cuts[i][0] = 1
    print(cuts)
    cuts = [x for x in cuts if x[0] == 0]
    print(cuts)
    cuts.sort(key=lambda x: x[1])
    print(cuts)
    cuts.insert(0, [0, 0])
    cuts.append([0, L])
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] -= cuts[i - 1][1]
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] += cuts[i - 1][1]
    print(cuts)
    for i in range(1, len(cuts)):
        cuts[i][1] -= cuts[i - 1][1]
    print(cuts)
    cuts = [x[1] for x in cuts]
    print(cuts)
    cuts.sort()
    for i in range(len(cuts)):
        if cuts[i] == 0:
            cuts[i] = cuts[i + 1]
    print(cuts)
    for i in range(len(cuts)):
        if cuts[i] == 0:
            cuts[i] = cuts[i - 1]
    print(cuts)
    cuts = [x for x in cuts if x != 0]
    print(cuts)
    for i in range(len(cuts)):
        print(cuts[i])

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            i = cut.index(x)
            print(cut[i+1]-cut[i-1])

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx+1] - cuts[idx-1])

=======
Suggestion 4

def main():
    L,Q = map(int,input().split())
    #print(L,Q)
    cut = []
    for i in range(Q):
        cut.append(list(map(int,input().split())))
        #print(cut[i])
    #print(cut)
    cut.sort(key = lambda x:x[1])
    #print(cut)
    #print(cut[0][1])
    #print(cut[1][1])
    #print(cut[2][1])
    #print(cut[3][1])
    #print(cut[4][1])
    #print(cut[5][1])
    #print(cut[6][1])
    #print(cut[7][1])
    #print(cut[8][1])
    #print(cut[9][1])
    ans = []
    for i in range(Q):
        if cut[i][0] == 1:
            cut.append([1,cut[i][1]])
            cut.append([1,L-cut[i][1]])
        else:
            #print(cut)
            #print(cut[i][1])
            #print(cut[i][1]-cut[i-1][1])
            #print(cut[i][1]-cut[i-1][1])
            ans.append(cut[i][1]-cut[i-1][1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 5

def solve():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            idx = cut.index(x)
            print(cut[idx+1] - cut[idx-1])

=======
Suggestion 6

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
            print(cuts[idx]-cuts[idx-1])

=======
Suggestion 7

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i + 1] - cut[i - 1])
                    break

=======
Suggestion 8

def readinput():
    L,Q = map(int,input().split())
    queries = []
    for _ in range(Q):
        c,x = map(int,input().split())
        queries.append((c,x))
    return (L,Q,queries)

=======
Suggestion 9

def main():
    L,Q = map(int,input().split())
    c = []
    x = []
    for i in range(Q):
        c_i,x_i = map(int,input().split())
        c.append(c_i)
        x.append(x_i)
    #print(c)
    #print(x)
    L1 = 0
    L2 = L
    for i in range(Q):
        if c[i] == 1:
            if x[i] < L2:
                L2 = x[i]
            if x[i] > L1:
                L1 = x[i]
        if c[i] == 2:
            if x[i] < L2:
                print(L2 - x[i])
            elif x[i] > L1:
                print(x[i] - L1)
            else:
                print(0)
    return 0

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    querys = []
    for _ in range(Q):
        querys.append(list(map(int, input().split())))
    #print(querys)
    #print(L, Q)
    #print(querys[0][0])
    #print(querys[0][1])
    #print(querys[1][0])
    #print(querys[1][1])
    ans = []
    for i in range(Q):
        if querys[i][0] == 1:
            ans.append(querys[i][1])
        elif querys[i][0] == 2:
            if querys[i][1] in ans:
                ans.remove(querys[i][1])
            else:
                ans.append(L - querys[i][1])
    for i in range(len(ans)):
        print(ans[i])

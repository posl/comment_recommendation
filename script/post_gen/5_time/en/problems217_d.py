Synthesizing 10/10 solutions

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
            n = len(cuts)
            for i in range(n):
                if cuts[i] == x:
                    print(cuts[i + 1] - cuts[i - 1])
                    break

=======
Suggestion 2

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
            print(cuts[idx+1]-cuts[idx-1])

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
            for j in range(len(cuts)):
                if cuts[j] == x:
                    print(cuts[j+1] - cuts[j-1])
                    break

=======
Suggestion 4

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        elif c == 2:
            cuts.sort()
            for i in range(len(cuts)):
                if cuts[i] == x:
                    print(cuts[i+1] - cuts[i-1])
                    break

=======
Suggestion 5

def main():
    L,Q = map(int,input().split())
    cuts = [0,L]
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for j in range(len(cuts)-1):
                if cuts[j] < x < cuts[j+1]:
                    print(cuts[j+1]-cuts[j])
                    break

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    cuts = []
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for j in range(len(cuts)):
                if cuts[j] > x:
                    break
            if j == 0:
                print(cuts[j])
            elif j == len(cuts):
                print(L - cuts[j - 1])
            else:
                print(cuts[j] - cuts[j - 1])

=======
Suggestion 7

def main():
    l,q = map(int,input().split())
    cuts = set([0,l])
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            cuts.add(x)
        else:
            print(max(cuts) - min(cuts))

=======
Suggestion 8

def get_input():
    l, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    return l, q, queries

=======
Suggestion 9

def findParent(parent, i):
    if parent[i] == i:
        return i
    return findParent(parent, parent[i])

=======
Suggestion 10

def get_input():
    return map(int, input().split())

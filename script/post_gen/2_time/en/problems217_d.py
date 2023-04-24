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
            cuts.append(x)
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx+1]-cuts[idx-1])

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
            left = cuts.index(x) - 1
            right = left + 1
            print(cuts[right] - cuts[left])

=======
Suggestion 3

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.append(x)
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx+1] - cuts[idx-1])

=======
Suggestion 4

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for i in range(len(cuts)):
                if cuts[i] == x:
                    print(cuts[i+1] - cuts[i-1])
                    break

=======
Suggestion 5

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            i = cuts.index(x)
            print(cuts[i] - cuts[i-1])

=======
Suggestion 6

def solve():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            print(cuts[cuts.index(x) + 1] - cuts[cuts.index(x) - 1])

=======
Suggestion 7

def main():
    L,Q = map(int,input().split())
    cuts = [0,L]
    for _ in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            i = cuts.index(x)
            print(cuts[i+1]-cuts[i-1])

=======
Suggestion 8

def problem217_d():
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
problem217_d()

=======
Suggestion 9

def cut_wood(L, Q, queries):
    wood = [L]
    for c, x in queries:
        if c == 1:
            wood.append(x)
        else:
            wood.sort()
            idx = wood.index(x)
            print(wood[idx+1]-wood[idx])

=======
Suggestion 10

def main():
    L,Q = map(int, input().split())
    #print(L,Q)

Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    #print(L, Q)
    #print(type(L), type(Q)

=======
Suggestion 2

def main():
    L,Q = map(int, input().split()

=======
Suggestion 3

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
            print(cut[i+1] - cut[i])

=======
Suggestion 4

def main():
    L, Q = map(int, input().split())
    mark = [0] * (L + 1)
    mark[1] = L
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = x
        else:
            ans = mark[x]
            for j in range(x, 0, -1):
                if mark[j] != 0:
                    ans = mark[j]
                    break
            print(ans)

=======
Suggestion 5

def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            idx = cuts.index(x)
            print(cuts[idx] - cuts[idx - 1])

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    mark = [0] * (L+1)
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        elif c == 2:
            l = 0
            r = L
            while r - l > 1:
                m = (l + r) // 2
                if sum(mark[:m+1]) >= x:
                    r = m
                else:
                    l = m
            print(r)

=======
Suggestion 7

def cut_wood(wood, mark):
    wood.sort()
    wood.append(mark)
    wood.append(0)
    wood.append(mark)
    wood.sort()
    return wood

=======
Suggestion 8

def main():
    l, q = map(int, input().split())
    mark = [0 for i in range(l+1)]
    mark[0] = 1
    mark[l] = 1
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = x
            while mark[left] == 0:
                left -= 1
            right = x
            while mark[right] == 0:
                right += 1
            print(right - left)

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    x = [0, L]
    for i in range(Q):
        c, q = map(int, input().split())
        if c == 1:
            x.append(q)
        else:
            x.sort()
            for j in range(len(x)):
                if x[j] == q:
                    print(x[j+1] - x[j-1])
                    break

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    print(L, Q)
    for i in range(Q):
        c, x = map(int, input().split())
        print(c, x)

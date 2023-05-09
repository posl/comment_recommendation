Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, q = map(int, input().split())
    a = [0]*q
    b = [0]*q
    c = [0]*q
    d = [0]*q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    for i1 in range(1, m+1):
        for i2 in range(i1, m+1):
            for i3 in range(i2, m+1):
                for i4 in range(i3, m+1):
                    for i5 in range(i4, m+1):
                        for i6 in range(i5, m+1):
                            for i7 in range(i6, m+1):
                                for i8 in range(i7, m+1):
                                    for i9 in range(i8, m+1):
                                        for i10 in range(i9, m+1):
                                            tmp = 0
                                            for i in range(q):
                                                if i10 - i9 == c[i] and i9 - i8 == c[i] and i8 - i7 == c[i] and i7 - i6 == c[i] and i6 - i5 == c[i] and i5 - i4 == c[i] and i4 - i3 == c[i] and i3 - i2 == c[i] and i2 - i1 == c[i] and i1 - 1 == c[i]:
                                                    tmp += d[i]
                                            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def readinput():
    n,m,q=map(int,input().split())
    abcd=[]
    for _ in range(q):
        abcd.append(list(map(int,input().split())))
    return n,m,q,abcd

=======
Suggestion 3

def score(A):
    s = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            s += d[i]
    return s

=======
Suggestion 4

def get_input():
    n, m, q = map(int, input().split())
    abcd = []
    for i in range(q):
        abcd.append(list(map(int, input().split())))
    return n, m, q, abcd

=======
Suggestion 5

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    ans = 0
    for a in range(1, m+1):
        for b in range(a, m+1):
            for c in range(b, m+1):
                for d in range(c, m+1):
                    for e in range(d, m+1):
                        for f in range(e, m+1):
                            for g in range(f, m+1):
                                for h in range(g, m+1):
                                    for i in range(h, m+1):
                                        for j in range(i, m+1):
                                            l = [a, b, c, d, e, f, g, h, i, j]
                                            tmp = 0
                                            for k in range(q):
                                                if l[abcd[k][1]-1] - l[abcd[k][0]-1] == abcd[k][2]:
                                                    tmp += abcd[k][3]
                                            if tmp > ans:
                                                ans = tmp
    print(ans)

=======
Suggestion 6

def score(a,b,c,d,seq):
    score = 0
    for i in range(len(a)):
        if seq[b[i]-1] - seq[a[i]-1] == c[i]:
            score += d[i]
    return score

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    abcd = []
    for i in range(Q):
        abcd.append(list(map(int, input().split())))
    ans = 0
    for A in list(combinations_with_replacement(range(1, M+1), N)):
        tmp = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def cal_score(A, Q, q):
    score = 0
    for i in range(Q):
        a = q[i][0]
        b = q[i][1]
        c = q[i][2]
        d = q[i][3]
        if A[b-1] - A[a-1] == c:
            score += d
    return score

=======
Suggestion 9

def get_input():
    return map(int, input().split())

n, m, q = get_input()
abcd = [list(get_input()) for _ in range(q)]

=======
Suggestion 10

def get_input():
    return map(int, input().split())

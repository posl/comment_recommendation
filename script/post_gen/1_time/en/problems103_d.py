Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    for i in range(M):
        if A[i] == B[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N - 1 - M)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    print(solve(n, m, a, b))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(solve(N, M, a, b))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    ans = 0
    for i in range(M):
        if i == 0:
            if a[i] > 1:
                ans += 1
        if i == M-1:
            if b[i] < N:
                ans += 1
        if i != 0 and i != M-1:
            if (a[i] - b[i-1]) > 1:
                ans += 1
    print(ans)
main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = 0
    for i in range(M):
        if right < AB[i][0]:
            ans += 1
            right = AB[i][1] - 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    cnt = 0
    bridge = 0
    for i in range(m):
        if ab[i][0] > bridge:
            cnt += 1
            bridge = ab[i][1] - 1
    print(cnt)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    count = 1
    bridge = bridges[0]
    for i in range(1, M):
        if bridge[1] < bridges[i][0]:
            bridge = bridges[i]
            count += 1
    print(M-count)

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    AB = [tuple(map(int,input().split())) for _ in range(M)]
    AB.sort()
    ans = 0
    cur = 0
    for a,b in AB:
        if a > cur:
            cur = b - 1
            ans += 1
        elif b <= cur:
            continue
        else:
            cur = b - 1
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    #print(N,M)

    #A = []
    #B = []
    #for i in range(M):
    #    a,b = map(int,input().split())
    #    A.append(a)
    #    B.append(b)
    #print(A)
    #print(B)

    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)

    A.sort()
    B.sort()
    #print(A)
    #print(B)

    #A = [1,2,3,4,5]
    #B = [1,2,3,4,5]

    Acount = 0
    Bcount = 0
    Acountmax = 0
    Bcountmax = 0
    for i in range(N-1):
        #print(i)
        #print(Acount)
        #print(Bcount)
        if A[Acount] == i+1:
            Acount += 1
        if B[Bcount] == i+1:
            Bcount += 1
        Acountmax = max(Acountmax,Acount)
        Bcountmax = max(Bcountmax,Bcount)
    #print(Acountmax)
    #print(Bcountmax)

    if Acountmax + Bcountmax >= M:
        print(M-(Acountmax+Bcountmax))
    else:
        print(M-(Acountmax+Bcountmax)+1)

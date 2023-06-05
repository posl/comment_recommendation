Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    print("hello world")

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)

    maxCount = 0
    for i in range(2**K):
        ball = [0]*N
        count = 0
        for j in range(K):
            if ((i>>j)&1):
                ball[D[j]-1] += 1
            else:
                ball[C[j]-1] += 1
        for j in range(M):
            if ball[A[j]-1] > 0 and ball[B[j]-1] > 0:
                count += 1
        if count > maxCount:
            maxCount = count
    print(maxCount)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(int(input().split()[0]))
        b.append(int(input().split()[1]))
    k = int(input())
    c = []
    d = []
    for i in range(k):
        c.append(int(input().split()[0]))
        d.append(int(input().split()[1]))
    ans = 0
    for i in range(2**k):
        dish = [0 for i in range(n)]
        for j in range(k):
            if ((i >> j) & 1):
                dish[c[j]-1] += 1
            else:
                dish[d[j]-1] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j]-1] >= 1 and dish[b[j]-1] >= 1:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 4

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # 遍历所有可能的状态
    ans = 0
    for i in range(2 ** K):
        dish = [False] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[C[j]-1] = True
            else:
                dish[D[j]-1] = True
        cnt = 0
        for j in range(M):
            if dish[A[j]-1] and dish[B[j]-1]:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [0] * N
        for j, (c, d) in enumerate(CD):
            if (i >> j) & 1:
                balls[c - 1] += 1
            else:
                balls[d - 1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a - 1] >= 1 and balls[b - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
solve()

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(M)]
    K = int(input())
    CD = [list(map(int,input().split())) for i in range(K)]
    ans = 0
    for i in range(2**K):
        tmp = [0]*N
        for j in range(K):
            if (i>>j)&1:
                tmp[CD[j][0]-1] += 1
            else:
                tmp[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if tmp[AB[j][0]-1] > 0 and tmp[AB[j][1]-1] > 0:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)
main()

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [False]*N
        for j in range(K):
            if (i>>j) & 1:
                balls[CD[j][0]-1] = True
            else:
                balls[CD[j][1]-1] = True
        cnt = 0
        for a, b in AB:
            if balls[a-1] and balls[b-1]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        s = set()
        for j in range(k):
            if ((i>>j)&1):
                s.add(cd[j][0])
            else:
                s.add(cd[j][1])
        cnt = 0
        for a,b in ab:
            if a in s and b in s:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        balls = [0] * (N + 1)
        for j in range(K):
            if i >> j & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1

        cnt = 0
        for a, b in AB:
            if balls[a] > 0 and balls[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

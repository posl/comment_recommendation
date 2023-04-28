Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        cnt = 0
        ball = [0]*N
        for j in range(K):
            if ((i >> j) & 1):
                ball[CD[j][0]-1] += 1
            else:
                ball[CD[j][1]-1] += 1
        for ab in AB:
            if ball[ab[0]-1] > 0 and ball[ab[1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    res = 0
    for i in range(2 ** K):
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        tmp = 0
        for a, b in AB:
            if balls[a] > 0 and balls[b] > 0:
                tmp += 1
        res = max(res, tmp)
    print(res)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        dish = [0] * (N + 1)
        for j in range(K):
            if ((i >> j) & 1) == 0:
                dish[CD[j][0]] = 1
            else:
                dish[CD[j][1]] = 1
        tmp = 0
        for a, b in AB:
            if dish[a] == 1 and dish[b] == 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if i >> j & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a-1] > 0 and balls[b-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[D[j]-1] += 1
            else:
                dish[C[j]-1] += 1
        cnt = 0
        for k in range(M):
            if dish[A[k]-1] >= 1 and dish[B[k]-1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

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
    ans = 0
    for i in range(2**K):
        cnt = [0]*N
        for j in range(K):
            if (i>>j)&1:
                cnt[D[j]-1] += 1
            else:
                cnt[C[j]-1] += 1
        tmp = 0
        for j in range(M):
            if cnt[A[j]-1] > 0 and cnt[B[j]-1] > 0:
                tmp += 1
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list()
    b = list()
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    k = int(input())
    c = list()
    d = list()
    for i in range(k):
        ci, di = map(int, input().split())
        c.append(ci)
        d.append(di)

    ans = 0
    for i in range(2**k):
        dish = [0]*n
        for j in range(k):
            if i>>j & 1:
                dish[c[j]-1] = 1
            else:
                dish[d[j]-1] = 1
        tmp = 0
        for j in range(m):
            if dish[a[j]-1] == 1 and dish[b[j]-1] == 1:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(lambda x:int(x)-1, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2**k):
        dish = [0]*n
        for j in range(k):
            dish[cd[j][(i>>j)&1]] += 1
        cnt = 0
        for a,b in ab:
            if dish[a] > 0 and dish[b] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()

conditions = []
for _ in range(M):
    conditions.append(read_ints())

K = int(input())

people = []
for _ in range(K):
    people.append(read_ints())

ans = 0
for i in range(2 ** K):
    balls = [0] * N
    for j in range(K):
        if (i >> j) & 1:
            balls[people[j][0] - 1] += 1
        else:
            balls[people[j][1] - 1] += 1

    cnt = 0
    for a, b in conditions:
        if balls[a - 1] > 0 and balls[b - 1] > 0:
            cnt += 1
    ans = max(ans, cnt)

print(ans)

=======
Suggestion 10

def countSatisfiedConditions(dishes, conditions, people):
    satisfiedConditions = 0
    for condition in conditions:
        if dishes[condition[0]-1] and dishes[condition[1]-1]:
            satisfiedConditions += 1
    return satisfiedConditions

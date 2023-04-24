Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        dish = [0] * N
        for j in range(K):
            dish[CD[j][(i >> j) & 1] - 1] += 1
        count = 0
        for j in range(M):
            if dish[AB[j][0] - 1] >= 1 and dish[AB[j][1] - 1] >= 1:
                count += 1
        ans = max(ans, count)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for bit in range(2**K):
        dish = [0] * N
        for i in range(K):
            dish[CD[i][(bit>>i)&1] - 1] += 1
        cnt = 0
        for i in range(M):
            if dish[AB[i][0] - 1] > 0 and dish[AB[i][1] - 1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    ans = 0
    for i in range(2 ** K):
        cnt = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                cnt[D[j] - 1] += 1
            else:
                cnt[C[j] - 1] += 1
        cnt2 = 0
        for j in range(M):
            if cnt[A[j] - 1] > 0 and cnt[B[j] - 1] > 0:
                cnt2 += 1
        ans = max(ans, cnt2)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int, input().split())))
    K = int(input())
    CD = []
    for _ in range(K):
        CD.append(list(map(int, input().split())))

    ans = 0
    for i in range(2**K):
        dish = [0 for _ in range(N)]
        for j in range(K):
            if i >> j & 1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]-1] > 0 and dish[AB[j][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    k = int(input())
    c = []
    d = []
    for i in range(k):
        ci, di = map(int, input().split())
        c.append(ci)
        d.append(di)

    ans = 0
    for i in range(2**k):
        dish = [0] * (n+1)
        for j in range(k):
            if (i >> j) & 1:
                dish[c[j]] += 1
            else:
                dish[d[j]] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j]] >= 1 and dish[b[j]] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    k = int(input())
    c = []
    d = []
    for i in range(k):
        ci, di = map(int, input().split())
        c.append(ci)
        d.append(di)
    ans = 0
    for i in range(2 ** k):
        dish = [0 for j in range(n)]
        for j in range(k):
            if (i >> j) & 1:
                dish[c[j] - 1] += 1
            else:
                dish[d[j] - 1] += 1
        count = 0
        for j in range(m):
            if dish[a[j] - 1] > 0 and dish[b[j] - 1] > 0:
                count += 1
        ans = max(ans, count)
    print(ans)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int,input().split())))
    K = int(input())
    CD = []
    for j in range(K):
        CD.append(list(map(int,input().split())))

    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][1]] += 1
            else:
                dish[CD[j][0]] += 1
        count = 0
        for k in range(M):
            if dish[AB[k][0]] > 0 and dish[AB[k][1]] > 0:
                count += 1
        ans = max(ans,count)
    print(ans)

=======
Suggestion 8

def get_input():
  n, m = map(int, input().split())
  ab = [list(map(int, input().split())) for _ in range(m)]
  k = int(input())
  cd = [list(map(int, input().split())) for _ in range(k)]
  return (n, m, ab, k, cd)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    k = int(input())
    c = []
    d = []
    for i in range(k):
        c.append(list(map(int,input().split())))
    ans = 0
    for i in range(2**k):
        dish = [0] * (n+1)
        for j in range(k):
            if ((i>>j) & 1):
                dish[c[j][0]] += 1
            else:
                dish[c[j][1]] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j][0]] >= 1 and dish[a[j][1]] >= 1:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 10

def main():
    # N, M
    N, M = map(int, input().split())

    # A_i, B_i
    AB = [list(map(int, input().split())) for _ in range(M)]

    # K
    K = int(input())

    # C_i, D_i
    CD = [list(map(int, input().split())) for _ in range(K)]

    # print(N, M, AB, K, CD)

    # print(N, M, AB, K, CD)

    max_count = 0
    for i in range(2 ** K):
        # print('i =', i)
        count = 0
        balls = [0] * N
        for j in range(K):
            # print('j =', j)
            # print('i >> j =', i >> j)
            if (i >> j) & 1:
                # print('i >> j & 1 =', i >> j & 1)
                balls[CD[j][0] - 1] += 1
            else:
                balls[CD[j][1] - 1] += 1
        # print('balls =', balls)
        for k in range(M):
            # print('k =', k)
            if balls[AB[k][0] - 1] > 0 and balls[AB[k][1] - 1] > 0:
                count += 1
        # print('count =', count)
        max_count = max(max_count, count)
        # print('max_count =', max_count)

    print(max_count)

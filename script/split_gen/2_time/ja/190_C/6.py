def main():
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
    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if (i >> j) & 1:
                balls[C[j]] += 1
            else:
                balls[D[j]] += 1
        tmp = 0
        for j in range(M):
            if balls[A[j]] > 0 and balls[B[j]] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

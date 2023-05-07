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
        cnt = 0
        dish = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                dish[C[j]] += 1
            else:
                dish[D[j]] += 1
        for j in range(M):
            if dish[A[j]] > 0 and dish[B[j]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

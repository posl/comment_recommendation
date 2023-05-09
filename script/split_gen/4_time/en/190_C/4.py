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

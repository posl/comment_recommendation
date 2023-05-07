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
        balls = [0] * (N+1)
        for j in range(K):
            if ((i >> j) & 1):
                balls[C[j]] += 1
            else:
                balls[D[j]] += 1
        cnt = 0
        for k in range(M):
            if balls[A[k]] > 0 and balls[B[k]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
main()

if __name__ == '__main__':
    main()
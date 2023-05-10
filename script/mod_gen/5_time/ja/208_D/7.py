def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
        C.append(c)
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if i > k or j > k:
                    continue
                ans += min(C[i]+C[j], C[k])
    print(ans)

if __name__ == '__main__':
    main()
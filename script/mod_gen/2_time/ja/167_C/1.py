def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        skill = [0]*M
        for j in range(N):
            if i>>j & 1:
                cost += C[j]
                for k in range(M):
                    skill[k] += A[j][k]
        if all(skill[k] >= X for k in range(M)):
            ans = min(ans, cost)
    print(-1 if ans == 10**9 else ans)

if __name__ == '__main__':
    main()
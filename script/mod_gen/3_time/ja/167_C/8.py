def main():
    N, M, X = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    ans = -1
    for i in range(2**N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j) & 1:
                cost += A[j][0]
                for k in range(M):
                    level[k] += A[j][k+1]
        if min(level) >= X:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    print(ans)

if __name__ == '__main__':
    main()
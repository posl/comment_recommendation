def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    X.sort(reverse=True)
    Y.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i + 1 >= C[j]:
                ans += Y[j] * ((i + 1) // C[j])
    print(ans)

if __name__ == '__main__':
    main()
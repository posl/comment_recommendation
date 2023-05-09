def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + L[i]
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
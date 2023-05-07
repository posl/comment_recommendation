def main():
    N = int(input())
    A = list(map(int, input().split()))
    minA = [0] * (N + 1)
    maxA = [0] * (N + 1)
    for i in range(N):
        minA[A[i]] = i + 1
        maxA[A[i]] = i + 1
    for i in range(1, N + 1):
        minA[i] = min(minA[i], minA[i - 1])
        maxA[N - i] = max(maxA[N - i], maxA[N - i + 1])
    ans = 0
    for i in range(1, N + 1):
        ans += maxA[i] - minA[i] + 1
    print(ans)

if __name__ == '__main__':
    main()
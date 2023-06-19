def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if A[j] - A[i - 1] == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
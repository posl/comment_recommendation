def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    ans = [0] * (N + 1)
    for i in range(N):
        ans[i + 1] = (A[i + 1] - A[i]) * (i + 1)
    for i in range(N):
        ans[i + 1] += ans[i]
    for i in range(N):
        if K <= ans[i + 1]:
            print(A[i] + (K - ans[i]) // (i + 1))
            break

if __name__ == '__main__':
    main()
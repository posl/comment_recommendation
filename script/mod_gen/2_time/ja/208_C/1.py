def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N:
            ans[i] += 1
            K -= 1
        else:
            ans[i] += K // N
            K -= K // N
    for i in range(N):
        if i < N - K:
            ans[i] += K // (N - i)
        else:
            ans[i] += K // (N - i) + 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()
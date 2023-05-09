def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N + 1)
    for i in range(N):
        if K >= (a[i + 1] - a[i]) * (i + 1):
            ans[i + 1] = ans[i] + (a[i + 1] - a[i])
            K -= (a[i + 1] - a[i]) * (i + 1)
        else:
            ans[i + 1] = ans[i] + K // (i + 1)
            K = 0
            break
    for i in range(N):
        if K >= N - i:
            ans[i + 1] += N - i
            K -= N - i
        else:
            ans[i + 1] += K
            K = 0
            break
    for i in range(N):
        print(ans[i + 1])

if __name__ == '__main__':
    main()
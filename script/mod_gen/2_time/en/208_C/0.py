def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            print(K)
    else:
        K -= N
        a.append(10 ** 9 + 1)
        ans = [0] * N
        for i in range(N):
            if a[i + 1] - a[i] == 1:
                ans[i] = K // N
            else:
                ans[i] = K // (N - i)
                break
        for i in range(N):
            print(ans[i] + N // N)

if __name__ == '__main__':
    main()
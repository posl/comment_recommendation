def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    #累積和
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    #累積和の差がKとなる組み合わせの個数を求める
    from collections import Counter
    cnt = Counter(A)
    ans = 0
    for i in range(N + 1):
        ans += cnt[A[i] - K]
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和を求める
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = (s[i] + A[i]) % M
    #累積和をソートする
    s.sort()
    ans = 0
    #s[i] == s[i + 1] となる要素の個数を求める
    cnt = 1
    for i in range(N):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
main()

if __name__ == '__main__':
    main()
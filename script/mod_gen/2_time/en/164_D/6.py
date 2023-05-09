def main():
    S = input()
    N = len(S)
    M = 2019
    cnt = [0 for _ in range(M)]
    cnt[0] = 1
    ten = 1
    x = 0
    for i in range(N-1, -1, -1):
        x = (x + int(S[i]) * ten) % M
        ten = (ten * 10) % M
        cnt[x] += 1
    ans = 0
    for i in range(M):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
def main():
    S = input()
    N = len(S)
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    for i in range(N):
        t = (t + int(S[N - 1 - i]) * pow(10, i, 2019)) % 2019
        cnt[t] += 1
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
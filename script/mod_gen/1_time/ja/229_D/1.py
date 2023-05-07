def main():
    S = input()
    K = int(input())
    N = len(S)
    cnt = 0
    ans = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            if cnt >= K:
                cnt -= K
                ans += K
                K = 0
            else:
                K -= cnt
                ans += cnt
                cnt = 0
    print(ans + min(cnt, K))

if __name__ == '__main__':
    main()
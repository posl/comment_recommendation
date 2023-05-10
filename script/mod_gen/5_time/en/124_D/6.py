def main():
    N, K = map(int, input().split())
    S = input()
    S = S + '0'
    cnt = 0
    start = 0
    if S[0] == '0':
        cnt = 1
    for i in range(1, N+1):
        if S[i-1] != S[i]:
            cnt += 1
        else:
            if cnt > 0:
                start += 1
            cnt = 0
    if cnt > 0:
        start += 1
    if start <= K:
        print(N)
    else:
        ans = 0
        cnt = 0
        tmp = 0
        for i in range(1, N+1):
            if S[i-1] != S[i]:
                cnt += 1
            else:
                if cnt > 0:
                    tmp += 1
                else:
                    ans += 1
                cnt = 0
            if tmp == K:
                break
        ans += cnt
        print(ans)

if __name__ == '__main__':
    main()
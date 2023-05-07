def main():
    N, K = map(int, input().split())
    S = input()
    S = S.replace('1', '2')
    S = S.replace('0', '1')
    S = S.replace('2', '0')
    S = list(S)
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            if S[j] == '1':
                cnt += 1
                if cnt > K:
                    break
            else:
                if cnt == K:
                    break
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()
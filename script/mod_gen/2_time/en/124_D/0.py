def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            cnt = 0
            for j in range(i, N):
                if S[j] == '0':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
        else:
            cnt = 0
            for j in range(i, N):
                if S[j] == '1':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    ans = min(N, ans + K * 2)
    print(ans)

if __name__ == '__main__':
    main()
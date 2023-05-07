def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    ans += K
    ans = min(ans, N)
    print(ans)

if __name__ == '__main__':
    main()
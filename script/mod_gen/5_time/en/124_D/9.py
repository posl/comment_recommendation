def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S = S + S
    S = list(map(int, S))
    #print(S)
    cnt = 0
    ans = 0
    for i in range(2 * N - 1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    #print(ans)
    ans = min(ans + 2 * K, N)
    print(ans)

if __name__ == '__main__':
    main()
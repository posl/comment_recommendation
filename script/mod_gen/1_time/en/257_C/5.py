def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    S = S[::-1]
    W = sorted(W)
    #print(S, W)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += N - i - W[i:].count(W[i])
        else:
            ans += W[:W.index(W[i])].count(W[i])
    print(ans)

if __name__ == '__main__':
    main()
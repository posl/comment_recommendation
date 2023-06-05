def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W_sum = sum(W)
    W_cumsum = [0] * (N+1)
    for i in range(N):
        W_cumsum[i+1] = W_cumsum[i] + W[i]
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans = max(ans, W_sum - W_cumsum[i+1])
        else:
            ans = max(ans, W_cumsum[i])
    print(ans)

if __name__ == '__main__':
    main()
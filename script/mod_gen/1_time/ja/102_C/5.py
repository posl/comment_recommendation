def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 累積和の最小値
    min_S = [0]
    for i in range(N):
        min_S.append(min(min_S[i], S[i+1]))
    # 累積和の最大値
    max_S = [0]
    for i in range(N):
        max_S.append(max(max_S[i], S[i+1]))
    ans = float('inf')
    for b in range(1, N+1):
        ans = min(ans, abs(min_S[b-1] + b - max_S[b-1] - b) + S[b-1] + S[N] - S[b])
    print(ans)

if __name__ == '__main__':
    main()
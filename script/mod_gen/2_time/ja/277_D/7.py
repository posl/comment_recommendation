def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 0 になるカードの数を数える
    count = [0] * M
    for a in A:
        count[a] += 1
    # 0 になるカードを選ぶ
    dp = [0] * M
    for i in range(M):
        dp[i] = count[i] + min(dp[(i-1)%M], dp[(i-2)%M])
    print(sum(A) - dp[0])

if __name__ == '__main__':
    main()
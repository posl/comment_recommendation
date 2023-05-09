def main():
    N = int(input())
    A = list(map(int, input().split()))
    # DP[i] = i番目の人が立てる最小のスツールの高さ
    DP = [0] * N
    for i in range(N):
        if i == 0:
            DP[i] = 0
        elif i == 1:
            DP[i] = max(0, A[i - 1] - A[i])
        else:
            DP[i] = max(0, A[i - 1] - A[i] + DP[i - 2])
    print(sum(DP))

if __name__ == '__main__':
    main()
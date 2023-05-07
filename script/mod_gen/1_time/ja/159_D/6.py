def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの要素数を数える
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1
    # Aの要素数を数える
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1
    # 答えを数える
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = cnt[i] * (cnt[i] - 1) // 2
    # 答えを出力する
    for i in range(1, N + 1):
        print(sum(ans) - ans[A[i - 1]] + (cnt[A[i - 1]] - 1) * (cnt[A[i - 1]] - 2) // 2)

if __name__ == '__main__':
    main()
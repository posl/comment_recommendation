def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    # Aの要素の値がB[i]であるものの個数をカウント
    cnt = [0] * (10**5 + 1)
    for i in range(N):
        cnt[A[i]] += 1
    # 答えを求める
    ans = sum(A)
    for i in range(Q):
        ans += cnt[B[i]] * (C[i] - B[i])
        cnt[C[i]] += cnt[B[i]]
        cnt[B[i]] = 0
        print(ans)

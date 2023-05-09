def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    # 累積和の値を M で割った余りを計算
    C = [b % M for b in B]
    # 余りの個数を数える
    D = [0] * M
    for c in C:
        D[c] += 1
    # 余りの個数を数える
    ans = 0
    for d in D:
        ans += d * (d - 1) // 2
    print(ans)

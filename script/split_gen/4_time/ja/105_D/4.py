def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 各 S[i] を M で割った余りを求める
    T = [x % M for x in S]
    # T の要素のうち、2つ以上同じものがあるものの数を求める
    from collections import Counter
    C = Counter(T)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

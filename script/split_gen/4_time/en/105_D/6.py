def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    acc = [0] * (N+1)
    for i in range(N):
        acc[i+1] = (acc[i] + A[i]) % M
    # 累積和の値をキーとして、同じ値を持つ要素の個数を数える
    from collections import Counter
    c = Counter(acc)
    ans = 0
    for v in c.values():
        ans += v * (v-1) // 2
    print(ans)

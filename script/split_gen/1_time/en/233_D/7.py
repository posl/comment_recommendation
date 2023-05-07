def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 累積和
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    
    # 累積和の差がKの倍数の個数
    from collections import Counter
    C = Counter(S)
    ans = 0
    for s in S:
        ans += C[s] * (C[s] - 1) // 2
        if (s - K) in C:
            ans -= C[s - K] * (C[s - K] - 1) // 2
    print(ans)

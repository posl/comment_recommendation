def main():
    import sys
    from math import gcd
    input = sys.stdin.readline
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # 最大公約数を求める
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    # D と最大公約数の最大公約数が 1 でないと
    # D の倍数が存在しない
    if gcd(g, D) != 1:
        print(-1)
        return
    # D の倍数が存在する場合、
    # D の倍数を K 個選ぶ
    # その中で最大のものが答え
    ans = 0
    for i in range(K):
        ans += D * i
    print(ans)

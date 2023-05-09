def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    #Xとの距離を求める
    x = [abs(i - X) for i in x]
    #Xとの距離の最大公約数を求める
    from math import gcd
    ans = x[0]
    for i in range(1, N):
        ans = gcd(ans, x[i])
    print(ans)

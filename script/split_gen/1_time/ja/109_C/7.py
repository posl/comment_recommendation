def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    # Xとxの差を取得
    x = [abs(X - i) for i in x]
    # 一番小さい値を取得
    ans = min(x)
    # 2つの値の最大公約数を求める
    for i in x:
        ans = gcd(ans, i)
    print(ans)

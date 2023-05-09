def main():
    #入力
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    #X と x[0] の差の最大公約数を求める
    d = x[0] - X
    for i in range(1, N):
        d = gcd(d, x[i] - X)
    
    #出力
    print(d)

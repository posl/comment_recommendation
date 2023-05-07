def main():
    A, B, K = map(int, input().split())
    # 1. A, Bの最大公約数を求める
    # 2. A, Bの最大公約数の約数を求める
    # 3. 2の約数を降順に並び替える
    # 4. K番目の約数を出力する
    # 1. A, Bの最大公約数を求める
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    c = gcd(A, B)
    # 2. A, Bの最大公約数の約数を求める
    d = []
    for i in range(1, c + 1):
        if c % i == 0:
            d.append(i)
    # 3. 2の約数を降順に並び替える
    d.sort(reverse=True)
    # 4. K番目の約数を出力する
    print(d[K - 1])

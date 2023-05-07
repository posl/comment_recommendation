def main():
    A, B, K = map(int, input().split())
    # A, B, K = 8, 12, 2
    # A, B, K = 100, 50, 4
    # A, B, K = 1, 1, 1
    # A, B, K = 100, 100, 100
    # A, B で割り切れる整数の個数
    c = 0
    # A, B で割り切れる整数の個数が K になった時の値
    ans = 0
    # A, B の最大公約数を求める
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    # A, B の最小公倍数を求める
    def lcm(a, b):
        return a * b // gcd(a, b)
    # A, B の最小公倍数を求める
    L = lcm(A, B)
    # 1 から L までの間で、A, B で割り切れる整数の個数を求める
    for i in range(1, L + 1):
        if i % A == 0 and i % B == 0:
            c += 1
            ans = i
        if c == K:
            break
    print(ans)

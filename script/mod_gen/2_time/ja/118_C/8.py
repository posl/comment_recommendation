def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最小公倍数を求める
    # 1. 2つの数の最大公約数を求める
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    # 2. 2つの数の最小公倍数を求める
    def lcm(a, b):
        return a*b//gcd(a,b)
    # 3. 3つ以上の数の最小公倍数を求める
    def lcmm(*args):
        return functools.reduce(lcm, args)
    print(lcmm(*A))

if __name__ == '__main__':
    main()
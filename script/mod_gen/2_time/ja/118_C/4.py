def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最小公倍数を求める
    from fractions import gcd
    from functools import reduce
    def lcm_base(x, y):
        return (x * y) // gcd(x, y)
    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)
    # 最小公倍数を求める
    ans = lcm(*A)
    print(ans)

if __name__ == '__main__':
    main()
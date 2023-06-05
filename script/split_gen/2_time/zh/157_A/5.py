def main():
    # 读入
    n, a, b = map(int, input().split())
    # 两个数的最大公约数
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    # 两个数的最小公倍数
    def lcm(x, y):
        return x * y // gcd(x, y)
    # 两个数的最小公倍数的倍数
    l = lcm(a, b)
    # 两个数的最小公倍数的倍数的个数
    m = n // l
    # 两个数的最小公倍数的倍数的最大个数
    max = 2 * m
    # 两个数的最小公倍数的倍数的最小个数
    min = 2 * m - 1
    # 两个数的最小公倍数的倍数的个数的差
    d = max - min
    # 两个数的最小公倍数的倍数的最小个数的最大值
    max_min = max + d * (n % l == 0)
    # 两个数的最小公倍数的倍数的最大个数的最小值
    min_max = min - d * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和
    sum = (max_min + min_max) * (n // l) // 2
    # 两个数的最小公倍数的倍数的个数的和的差
    diff = max_min - min_max
    # 两个数的最小公倍数的倍数的个数的和的差的最小值
    min_sum = sum - diff * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和的差的最大值
    max_sum = sum + diff * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和

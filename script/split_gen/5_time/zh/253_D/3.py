def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 解决方案
    # a, b的最小公倍数
    lcm = a * b // math.gcd(a, b)
    # 1-n之间能被a或b整除的数的个数
    cnt = n // a + n // b - n // lcm
    # 1-n之间不能被a或b整除的数的个数
    cnt = n - cnt
    # 1-n之间不能被a或b整除的数的和
    ans = (1 + cnt) * cnt // 2
    # 输出
    print(ans)

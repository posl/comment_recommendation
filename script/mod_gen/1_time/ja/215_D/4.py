def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #gcd
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    #lcm
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    #lcm
    def lcm_list(A):
        return reduce(lcm, A)
    #lcm
    def lcm_list2(A):
        return functools.reduce(lcm, A)
    #gcd
    def gcd_list(A):
        return reduce(gcd, A)
    #gcd
    def gcd_list2(A):
        return functools.reduce(gcd, A)
    #最小公倍数
    lcm_A = lcm_list2(A)
    #最大公約数
    gcd_A = gcd_list2(A)
    #最小公倍数の約数を列挙
    div_lcm_A = []
    for i in range(1, int(lcm_A ** 0.5) + 1):
        if lcm_A % i == 0:
            div_lcm_A.append(i)
            if i != lcm_A // i:
                div_lcm_A.append(lcm_A // i)
    #最大公約数の約数を列挙
    div_gcd_A = []
    for i in range(1, int(gcd_A ** 0.5) + 1):
        if gcd_A % i == 0:
            div_gcd_A.append(i)
            if i != gcd_A // i:
                div_gcd_A.append(gcd_A // i)
    #最小公倍数の約数のうち、最大公約数の約数でないものを列挙
    div_lcm_A2 = []
    for i in div_lcm_A:
        if i not in div_gcd_A:
            div_lcm_A2.append(i)
    #最小公倍数の約数のうち、最大公約数の約数でないものを列挙
    div_lcm_A3 = []
    for i in div_lcm_A2:
        if i <= M:
            div_lcm

if __name__ == '__main__':
    main()
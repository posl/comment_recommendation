def main():
    n, a, b = map(int, input().split())
    # 全体からaの倍数+bの倍数の和を引く
    # aの倍数+bの倍数はaとbの最小公倍数の倍数
    # aとbの最小公倍数 = a*b / 最大公約数
    # 最大公約数はユークリッドの互除法を使う
    print(n * (n + 1) // 2 - (n // a + n // b - n // (a * b // gcd(a, b))) * (n // a + n // b - n // (a * b // gcd(a, b)) + 1) // 2)

if __name__ == '__main__':
    main()
def func():
    A, B, C, D, E, F = map(int, input().split())
    if A * B * C >= D * E * F:
        print((A * B * C) % 998244353 - (D * E * F) % 998244353)
    else:
        print((D * E * F) % 998244353 - (A * B * C) % 998244353)

if __name__ == '__main__':
    func()
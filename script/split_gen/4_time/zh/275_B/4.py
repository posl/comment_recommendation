def main():
    A, B, C, D, E, F = [int(i) for i in input().split()]
    print((A * B * C - D * E * F) % 998244353)

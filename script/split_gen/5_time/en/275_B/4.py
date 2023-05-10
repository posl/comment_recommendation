def main():
    # input
    A, B, C, D, E, F = map(int, input().split())
    # compute
    # output
    print((A*B*C-D*E*F) % 998244353)

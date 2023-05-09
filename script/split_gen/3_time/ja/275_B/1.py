def main():
    A, B, C, D, E, F = map(int, input().split())
    mod = 998244353
    ans = (A*B*C - D*E*F) % mod
    print(ans)

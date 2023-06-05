def main():
    # 输入
    A, B, C, D, E, F = map(int, input().split())
    # 乘法的结果
    ABC = A * B * C
    DEF = D * E * F
    # 乘法的结果对998244353取模
    ABC = ABC % 998244353
    DEF = DEF % 998244353
    # 输出
    print((ABC - DEF) % 998244353)

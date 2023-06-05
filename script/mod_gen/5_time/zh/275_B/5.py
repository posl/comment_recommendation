def problems275_b():
    #输入
    A, B, C, D, E, F = map(int, input().split())
    #计算
    ans = (A*B*C) % 998244353 - (D*E*F) % 998244353
    #输出
    print(ans % 998244353)

if __name__ == '__main__':
    problems275_b()
def problems275_b():
    A,B,C,D,E,F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

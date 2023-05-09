def input_to_int():
    return map(int,input().split())
A,B,C,D,E,F = input_to_int()
print(((A*B*C)-(D*E*F))%998244353)

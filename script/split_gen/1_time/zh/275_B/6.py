def main():
    A, B, C, D, E, F = map(int, input().split())
    #print(A, B, C, D, E, F)
    #print(A*B*C, D*E*F)
    if A*B*C >= D*E*F:
        print((A*B*C - D*E*F) % 998244353)
    else:
        print(0)

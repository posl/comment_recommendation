def main():
    A,B,C,D,E,F = map(int,input().split())
    if A*B*C >= D*E*F:
        result = (A*B*C) - (D*E*F)
    else:
        result = (D*E*F) - (A*B*C)
    print(result%998244353)
main()

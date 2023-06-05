def main():
    A,B,C,D,E,F=map(int,input().split())
    if A*B*C>=D*E*F:
        print((A*B*C-D*E*F)%998244353)
    else:
        print((D*E*F-A*B*C)%998244353)
main()

def main():
    # Read data
    A,B,C,D,E,F = map(int,input().split())
    # Calculate (A× B× C)-(D× E× F) mod 998244353
    print((A*B*C-D*E*F)%998244353)

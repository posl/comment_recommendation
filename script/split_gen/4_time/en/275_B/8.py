def main():
    #input
    A,B,C,D,E,F = map(int,input().split())
    #compute
    #A× B× C≧ D× E× F
    #A× B× C - D× E× F ≧ 0
    #A× B× C - D× E× F mod 998244353
    print((A*B*C - D*E*F)%998244353)

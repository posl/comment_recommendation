def problems275_b(A,B,C,D,E,F):
    if A*B*C>=D*E*F:
        return (A*B*C-D*E*F)%998244353
    else:
        return (D*E*F-A*B*C)%998244353

if __name__ == '__main__':
    problems275_b()
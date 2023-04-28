Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # A, B, C, D, E, F = map(int, input().split())
    A, B, C, D, E, F = 2, 3, 5, 1, 2, 4
    # A, B, C, D, E, F = 1, 1, 1000000000, 0, 0, 0
    # A, B, C, D, E, F = 10

=======
Suggestion 2

def main():
    A, B, C, D, E, F = map(int, input().split())
    print(((A*B*C)-(D*E*F))%998244353)

=======
Suggestion 3

def main():
    A, B, C, D, E, F = map(int, input().split())
    print((A*B*C-D*E*F)%998244353)

=======
Suggestion 4

def problems275_b():
    A, B, C, D, E, F = map(int, input().split())
    print(((((A % 998244353) * (B % 998244353)) % 998244353) * (C % 998244353)) % 998244353 - ((((D % 998244353) * (E % 998244353)) % 998244353) * (F % 998244353)) % 998244353) % 998244353)

=======
Suggestion 5

def main():
    # input
    a, b, c, d, e, f = map(int, input().split())
    # compute
    x = (a * b * c) % 998244353
    y = (d * e * f) % 998244353
    # output
    print((x - y) % 998244353)

=======
Suggestion 6

def main():
    a,b,c,d,e,f = map(int,input().split())
    print((a*b*c-d*e*f)%998244353)

=======
Suggestion 7

def main():
    A, B, C, D, E, F = map(int, input().split())
    #print(A, B, C, D, E, F)
    #print((A*B*C)%(998244353))
    #print((D*E*F)%(998244353))
    print(((A*B*C)%(998244353)-(D*E*F)%(998244353))%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)-(D*E*F))
    #print((A*B*C)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))
    #print((A*B*C)%(998244353)-(D*E*F)%(998244353))

=======
Suggestion 8

def input_to_int():
    return map(int,input().split())

A,B,C,D,E,F = input_to_int()

print(((A*B*C)-(D*E*F))%998244353)

=======
Suggestion 9

def main():
    #input
    A,B,C,D,E,F = map(int,input().split())
    #compute
    #A× B× C≧ D× E× F
    #A× B× C - D× E× F ≧ 0
    #A× B× C - D× E× F mod 998244353
    print((A*B*C - D*E*F)%998244353)

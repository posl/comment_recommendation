def solve():
    A, B, C, X = map(int, input().split())
    if X<=A:
        print(1.0)
        return
    if X>B:
        print(0.0)
        return
    if A==B:
        print(0.0)
        return
    if C==0:
        print(0.0)
        return
    if C==1:
        print(1.0/(B-A))
        return
    if C==B-A:
        print(1.0)
        return
    if C==2:
        print(1.0/(B-A)*(1.0/(B-A-1)))
        return
    if C==3:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2)))
        return
    if C==4:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3)))
        return
    if C==5:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4)))
        return
    if C==6:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5)))
        return
    if C==7:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5))*(1.0/(B-A-6)))
        return
    if C==8:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5))*(1.0/(B-A-6))*(1.0/(B-A-7)))

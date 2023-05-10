def solve(A,B,C):
    if C%2==0:
        A=abs(A)
        B=abs(B)
    if A==B:
        print("=")
    elif A>B:
        print(">")
    else:
        print("<")
    return 0

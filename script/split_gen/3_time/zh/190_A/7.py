def solve(A,B,C):
    if C==0:
        if A>B:
            print("Takahashi")
        else:
            print("Aoki")
    if C==1:
        if A>=B:
            print("Takahashi")
        else:
            print("Aoki")

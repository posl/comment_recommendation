def solve(A,B,C):
    if A==B==C:
        return 1
    else:
        return 2*A/(A+B+C)+solve(A+1,B-1,C)+solve(A,B+1,C-1)

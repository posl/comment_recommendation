def solve(A,B):
    for i in range(1,7):
        for j in range(1,7):
            if i+j==B:
                return True
    return False
A,B=map(int,input().split())

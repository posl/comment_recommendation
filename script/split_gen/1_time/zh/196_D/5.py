def solve(H,W,A,B):
    if A==0 and B==0:
        return 1
    if A==0:
        return solve(W,H,B,A)
    if H==1:
        return solve(W,1,B-1,0)
    if W==1:
        return solve(1,H,B-1,0)
    return solve(H-1,W,A-1,B)+solve(H,W-1,A-1,B)
H,W,A,B=map(int,input().split())
print(solve(H,W,A,B))

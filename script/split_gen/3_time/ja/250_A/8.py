def problems250_a():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(4 if R==1 or R==H or C==1 or C==W else 8)

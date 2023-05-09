def main():
    W,H,x,y = map(int,input().split())
    import math
    S = W*H/2
    if x*2 == W and y*2 == H:
        M = 1
    else:
        M = 0
    print(S,M)

def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())
    #compute
    if L1 <= L2 <= R1:
        if R2 <= R1:
            ans = R2-L2
        else:
            ans = R1-L2
    elif L2 <= L1 <= R2:
        if R1 <= R2:
            ans = R1-L1
        else:
            ans = R2-L1
    else:
        ans = 0
    #output
    print(ans)

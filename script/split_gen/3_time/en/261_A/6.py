def main():
    #input
    l1,r1,l2,r2 = map(int,input().split())
    #compute
    if r1 < l2:
        ans = 0
    elif r2 < l1:
        ans = 0
    else:
        ans = min(r1,r2) - max(l1,l2)
    #output
    print(ans)

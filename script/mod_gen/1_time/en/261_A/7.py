def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())
    #calc
    if L1 < L2:
        if R1 < L2:
            ans = 0
        elif R1 < R2:
            ans = R1 - L2
        else:
            ans = R2 - L2
    else:
        if R2 < L1:
            ans = 0
        elif R2 < R1:
            ans = R2 - L1
        else:
            ans = R1 - L1
    #output
    print(ans)

if __name__ == '__main__':
    main()
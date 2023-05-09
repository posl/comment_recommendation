def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())
    #output
    if L1<=L2 and L2<=R1 and R1<=R2:
        print(R1-L2)
    elif L2<=L1 and L1<=R2 and R2<=R1:
        print(R2-L1)
    elif L2<=L1 and L1<=R1 and R1<=R2:
        print(R1-L1)
    elif L1<=L2 and L2<=R2 and R2<=R1:
        print(R2-L2)
    else:
        print(0)
    return

if __name__ == '__main__':
    main()
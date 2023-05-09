def main():
    L1, R1, L2, R2 = input().split()
    L1 = int(L1)
    R1 = int(R1)
    L2 = int(L2)
    R2 = int(R2)
    if L2 <= R1 and L1 <= R2:
        if L1 <= L2 and R1 <= R2:
            print(R1 - L2)
        elif L2 <= L1 and R2 <= R1:
            print(R2 - L1)
        elif L1 <= L2 and R2 <= R1:
            print(R2 - L2)
        elif L2 <= L1 and R1 <= R2:
            print(R1 - L1)
    else:
        print(0)

if __name__ == '__main__':
    main()
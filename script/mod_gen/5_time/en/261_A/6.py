def main():
    # input
    L1, R1, L2, R2 = map(int, input().split())
    # compute
    # output
    if (L1 <= L2 <= R1 <= R2) or (L2 <= L1 <= R2 <= R1):
        print(R1 - L2)
    elif (L2 <= L1 <= R1 <= R2) or (L1 <= L2 <= R2 <= R1):
        print(R2 - L1)
    else:
        print(0)

if __name__ == '__main__':
    main()
def main():
    # Read input
    L1, R1, L2, R2 = map(int, input().split())
    # Check if L1 is between L2 and R2
    if L1 >= L2 and L1 <= R2:
        # Check if R1 is between L2 and R2
        if R1 >= L2 and R1 <= R2:
            print(R1 - L1)
        else:
            print(R2 - L1)
    # Check if L2 is between L1 and R1
    elif L2 >= L1 and L2 <= R1:
        # Check if R2 is between L1 and R1
        if R2 >= L1 and R2 <= R1:
            print(R2 - L2)
        else:
            print(R1 - L2)
    else:
        print(0)

if __name__ == '__main__':
    main()
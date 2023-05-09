def main():
    # Read input
    L1, R1, L2, R2 = map(int, input().split())
    # Calculate the length of the part of the line painted both red and blue
    result = 0
    if L1 < L2:
        if R1 < L2:
            result = 0
        elif R1 < R2:
            result = R1 - L2
        else:
            result = R2 - L2
    else:
        if R2 < L1:
            result = 0
        elif R2 < R1:
            result = R2 - L1
        else:
            result = R1 - L1
    # Output
    print(result)

if __name__ == '__main__':
    main()
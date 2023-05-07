def main():
    # Read the input
    L1, R1, L2, R2 = map(int, input().split())
    # Find the length of the part of the line painted both red and blue
    if R1 >= L2 and R1 <= R2:
        length = R1 - L2
    elif R2 >= L1 and R2 <= R1:
        length = R2 - L1
    else:
        length = 0
    # Output the result
    print(length)

if __name__ == '__main__':
    main()
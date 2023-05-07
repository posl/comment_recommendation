def main():
    #read input
    L1, R1, L2, R2 = map(int, input().split())
    #find the length of the part of the line painted both red and blue, as an integer.
    if R1 < L2:
        print(0)
    elif R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

if __name__ == '__main__':
    main()
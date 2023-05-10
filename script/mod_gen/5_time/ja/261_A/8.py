def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 <= L2 and L2 < R1:
        if R1 <= R2:
            print(R1 - L2)
        else:
            print(R2 - L2)
    elif L2 <= L1 and L1 < R2:
        if R2 <= R1:
            print(R2 - L1)
        else:
            print(R1 - L1)
    else:
        print(0)

if __name__ == '__main__':
    main()
def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 <= L2 or R2 <= L1:
        print(0)
    elif L1 <= L2 and R1 <= R2:
        print(R1 - L2)
    elif L1 <= L2 and R1 >= R2:
        print(R2 - L2)
    elif L1 >= L2 and R1 <= R2:
        print(R1 - L1)
    elif L1 >= L2 and R1 >= R2:
        print(R2 - L1)

if __name__ == '__main__':
    main()
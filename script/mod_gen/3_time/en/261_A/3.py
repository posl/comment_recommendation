def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 < L2:
        if R1 < L2:
            print(0)
        else:
            print(min(R1, R2) - L2)
    else:
        if R2 < L1:
            print(0)
        else:
            print(min(R1, R2) - L1)

if __name__ == '__main__':
    main()
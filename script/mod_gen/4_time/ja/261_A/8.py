def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 <= R1 and L1 <= R2:
        print(max(L2, L1), min(R2, R1))
    else:
        print(0)

if __name__ == '__main__':
    main()
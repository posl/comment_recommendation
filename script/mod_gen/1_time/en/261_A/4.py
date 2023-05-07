def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R2 < L1 or R1 < L2:
        print(0)
        return
    print(min(R1, R2) - max(L1, L2))

if __name__ == '__main__':
    main()
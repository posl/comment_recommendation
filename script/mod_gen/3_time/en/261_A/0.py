def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 < L2 or R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))
main()

if __name__ == '__main__':
    main()
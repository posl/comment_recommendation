def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 <= R1:
        print(max(R1, R2) - L2)
    elif L1 <= R2:
        print(max(R1, R2) - L1)
    else:
        print(0)

if __name__ == '__main__':
    main()
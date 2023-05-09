def main():
    # read input
    L1, R1, L2, R2 = map(int, input().split())
    # calc
    if R1 < L2:
        result = 0
    elif R2 < L1:
        result = 0
    else:
        result = min(R1, R2) - max(L1, L2)
    # print
    print(result)

if __name__ == '__main__':
    main()
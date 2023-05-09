def main():
    #Read the input
    L1, R1, L2, R2 = map(int, input().split())
    #Check if the intervals overlap
    if L2 >= R1 or L1 >= R2:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

if __name__ == '__main__':
    main()
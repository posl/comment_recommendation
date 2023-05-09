def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    # output
    if (A==B and B==C and D==E) or (A==B and C==D and D==E):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
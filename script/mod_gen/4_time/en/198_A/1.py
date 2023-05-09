def main():
    # input
    N = int(input())
    # compute
    # output
    if N%2 == 0:
        print(int(N/2-1))
    else:
        print(int(N/2))

if __name__ == '__main__':
    main()
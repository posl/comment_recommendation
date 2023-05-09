def main():
    # read input
    D, N = map(int, input().split())
    # compute output
    if N == 100:
        N += 1
    output = N * 100**D
    # print output
    print(output)
main()

if __name__ == '__main__':
    main()
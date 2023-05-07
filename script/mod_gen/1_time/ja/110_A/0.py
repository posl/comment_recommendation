def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    # output
    print(max(10 * A + B + C, A + 10 * B + C, A + B + 10 * C))

if __name__ == '__main__':
    main()
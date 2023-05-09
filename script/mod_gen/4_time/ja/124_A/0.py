def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    print(max(A+A-1, A+B, B+B-1))

if __name__ == '__main__':
    main()
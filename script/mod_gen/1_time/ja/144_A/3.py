def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A * B)

if __name__ == '__main__':
    main()
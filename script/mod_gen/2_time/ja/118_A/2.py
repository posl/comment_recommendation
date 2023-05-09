def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if B % A == 0:
        print(A+B)
    else:
        print(B-A)

if __name__ == '__main__':
    main()
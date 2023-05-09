def main():
    # input
    A = list(map(int, input().split()))
    # compute
    A.sort()
    # output
    print(A[2]-A[0])

if __name__ == '__main__':
    main()
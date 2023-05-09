def main():
    # input
    n = int(input())
    a = [int(i) for i in input().split()]
    # compute
    b = [0] * n
    b[0] = a[0]
    for i in range(1,n):
        b[i] = a[i] - b[i-1] // 2
    b[0] = a[0] - b[-1] // 2
    # output
    print(" ".join([str(i) for i in b]))

if __name__ == '__main__':
    main()
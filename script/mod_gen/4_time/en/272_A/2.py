def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    # compute
    sum = 0
    for i in range(n):
        sum += a[i]
    # output
    print(sum)

if __name__ == '__main__':
    main()
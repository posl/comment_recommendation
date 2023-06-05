def main():
    # input
    n = int(input())
    # compute
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            break
    # output
    print(i)

if __name__ == '__main__':
    main()
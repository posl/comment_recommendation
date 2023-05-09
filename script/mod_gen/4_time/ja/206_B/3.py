def main():
    # input
    N = int(input())
    # compute
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            break
    # output
    print(i)

if __name__ == '__main__':
    main()
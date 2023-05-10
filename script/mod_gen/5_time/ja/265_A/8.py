def main():
    # input
    X, Y, N = map(int, input().split())
    # compute
    ans = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            ans += X
        else:
            ans += Y
    # output
    print(ans)

if __name__ == '__main__':
    main()
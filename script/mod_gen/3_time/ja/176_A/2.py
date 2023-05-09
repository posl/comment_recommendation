def main():
    # input
    N, X, T = map(int, input().split())
    # compute
    ans = (N+X-1)//X * T
    # output
    print(ans)

if __name__ == '__main__':
    main()
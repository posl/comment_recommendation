def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    # compute
    if 0 in As:
        print(0)
        exit()
    ans = 1
    for A in As:
        ans *= A
        if ans > 10**18:
            print(-1)
            exit()
    # output
    print(ans)

if __name__ == '__main__':
    main()
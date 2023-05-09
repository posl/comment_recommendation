def main():
    # input
    N, X = map(int, input().split())
    S = input()
    # compute
    ans = X
    for s in S:
        if s == 'o':
            ans += 1
        elif s == 'x' and ans > 0:
            ans -= 1
    # output
    print(ans)

if __name__ == '__main__':
    main()
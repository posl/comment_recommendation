def main():
    # input
    n, x = map(int, input().split())
    s = input()
    # compute
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans //= 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    # output
    print(ans)

if __name__ == '__main__':
    main()
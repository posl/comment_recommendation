def main():
    s = input()
    n = len(s)
    ans = [0] * n
    flag = 0
    for i in range(n):
        if s[i] == 'R':
            flag += 1
        else:
            if flag % 2 == 0:
                ans[flag] += 1
            else:
                ans[flag - 1] += 1
            flag = 0
    flag = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            flag += 1
        else:
            if flag % 2 == 0:
                ans[n - 1 - flag] += 1
            else:
                ans[n - flag] += 1
            flag = 0
    print(*ans)

if __name__ == '__main__':
    main()
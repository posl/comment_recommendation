def main():
    s = input()
    n = len(s)
    a = [0] * n
    for i in range(n):
        a[i] = int(s[i])
    ans = -1
    for i in range(n):
        if a[i] % 3 == 0:
            ans = 0
            break
        if a[i] % 3 == 1:
            if ans == -1:
                ans = 1
            elif ans == 2:
                ans = 1
            else:
                ans = 2
        if a[i] % 3 == 2:
            if ans == -1:
                ans = 2
            elif ans == 1:
                ans = 2
            else:
                ans = 1
    if ans == -1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
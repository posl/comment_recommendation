def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = (ans + 1) // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2
    print(ans)

if __name__ == '__main__':
    main()
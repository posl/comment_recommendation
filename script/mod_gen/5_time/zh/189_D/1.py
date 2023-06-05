def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s[0] == 'AND':
        ans = 1
    else:
        ans = 0
    for i in range(1, n):
        if s[i] == 'AND':
            ans *= 2
        else:
            ans = ans * 2 + 1
    print(2 ** (n + 1) - ans)

if __name__ == '__main__':
    main()
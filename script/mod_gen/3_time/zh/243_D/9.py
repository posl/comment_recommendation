def main():
    n, x = map(int, input().split())
    s = input()
    x -= 1
    for i in range(n):
        if s[i] == 'U':
            x = x // 2
        elif s[i] == 'L':
            x = x * 2
        else:
            x = x * 2 + 1
    print(x + 1)

if __name__ == '__main__':
    main()
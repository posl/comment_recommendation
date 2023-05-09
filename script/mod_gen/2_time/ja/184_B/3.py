def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif s[i] == 'x':
            if x > 0:
                x -= 1
            else:
                pass
    print(x)

if __name__ == '__main__':
    main()
def main():
    s = input()
    if s[0] == 'o':
        total = 10 ** 4
    else:
        total = 9 * 10 ** 4
    for i in range(1, len(s)):
        if s[i] == 'o':
            total *= 9 - i
        elif s[i] == 'x':
            total *= 10 - 1 - 9 + i
        else:
            total *= 10 - i
    print(total)

if __name__ == '__main__':
    main()
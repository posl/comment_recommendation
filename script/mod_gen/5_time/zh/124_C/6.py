def main():
    s = input()
    n = 0
    for i in range(len(s)):
        if s[i] == '1' and i % 2 == 0:
            n += 1
        elif s[i] == '0' and i % 2 == 1:
            n += 1
    print(min(n, len(s) - n))

if __name__ == '__main__':
    main()
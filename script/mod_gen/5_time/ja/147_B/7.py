def main():
    s = input()
    l = len(s)
    c = 0
    for i in range(l):
        if s[i] != s[l - 1 - i]:
            c += 1
    print(c // 2)

if __name__ == '__main__':
    main()
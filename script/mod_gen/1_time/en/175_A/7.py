def main():
    s = input()
    n = 0
    m = 0
    for i in range(len(s)):
        if s[i] == "R":
            n += 1
            m = max(n, m)
        else:
            n = 0
    print(m)

if __name__ == '__main__':
    main()
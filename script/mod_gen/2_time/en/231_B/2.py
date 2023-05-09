def main():
    n = int(input())
    s = [input() for i in range(n)]
    c = [s.count(i) for i in s]
    print(s[c.index(max(c))])

if __name__ == '__main__':
    main()
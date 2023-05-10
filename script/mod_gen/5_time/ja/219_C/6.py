def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    x = list(x)
    x.sort()
    d = {}
    for i in range(26):
        d[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(d))
    s.sort()
    for i in range(n):
        s[i] = s[i].translate(str.maketrans({v: k for k, v in d.items()}))
    print(*s, sep='\n')

if __name__ == '__main__':
    main()
def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(x[j], chr(97+j))
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(chr(97+j), x[j])
    s.sort()
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(x[j], chr(97+j))
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()
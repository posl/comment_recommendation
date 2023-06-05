def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    xdict = {}
    for i in range(26):
        xdict[x[i]] = chr(i+97)
    for i in range(n):
        for j in range(len(s[i])):
            s[i] = s[i].replace(s[i][j], xdict[s[i][j]])
    s.sort()
    for i in range(n):
        for j in range(len(s[i])):
            s[i] = s[i].replace(s[i][j], x[xdict[s[i][j]]-97])
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()
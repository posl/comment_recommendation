def main():
    # input
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # compute
    d = {}
    for i in range(26):
        d[x[i]] = chr(i+97)
    for i in range(n):
        for j in range(len(s[i])):
            s[i] = s[i].replace(s[i][j], d[s[i][j]])
    # output
    for i in sorted(s):
        print(i)

if __name__ == '__main__':
    main()
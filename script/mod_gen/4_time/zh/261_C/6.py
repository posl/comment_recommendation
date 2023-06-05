def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            x = s[:i].count(s[i])
            print(s[i]+"("+str(x)+")")

if __name__ == '__main__':
    main()
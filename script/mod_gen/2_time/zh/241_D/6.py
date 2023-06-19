def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == "1":
            a.append(int(s[1]))
        elif s[0] == "2":
            a.sort()
            if len(a) < int(s[2]):
                print(-1)
            else:
                print(a[-int(s[2])])
        elif s[0] == "3":
            a.sort()
            if len(a) < int(s[2]):
                print(-1)
            else:
                print(a[int(s[2])-1])

if __name__ == '__main__':
    main()
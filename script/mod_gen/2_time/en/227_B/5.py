def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if n == 1:
        print(1)
        exit()
    if n == 2:
        if s[0] == s[1]:
            print(2)
        else:
            print(1)
        exit()
    if n == 3:
        if s[0] + s[1] == s[2]:
            print(1)
            exit()
        else:
            print(2)
            exit()
    if n == 4:
        if s[0] + s[1] == s[2] + s[3]:
            print(2)
            exit()
        if s[0] + s[1] == s[2]:
            print(2)
            exit()
        if s[0] + s[1] == s[3]:
            print(2)
            exit()
        if s[0] + s[2] == s[1] + s[3]:
            print(2)
            exit()
        if s[0] + s[2] == s[1]:
            print(2)
            exit()
        if s[0] + s[2] == s[3]:
            print(2)
            exit()
        if s[0] + s[3] == s[1] + s[2]:
            print(2)
            exit()
        if s[0] + s[3] == s[1]:
            print(2)
            exit()
        if s[0] + s[3] == s[2]:
            print(2)
            exit()
        if s[1] + s[2] == s[0] + s[3]:
            print(2)
            exit()
        if s[1] + s[2] == s[0]:
            print(2)
            exit()
        if s[1] + s[2] == s[3]:
            print(2)
            exit()
        if s[1] + s[3] == s[0] + s[2]:
            print(2)
            exit()
        if s[1] + s[3] == s[0]:
            print(2)
            exit()
        if s[1] + s[3] == s[2]:
            print

if __name__ == '__main__':
    main()
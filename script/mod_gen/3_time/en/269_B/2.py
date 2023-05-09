def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i].find('#') != -1:
            if a == 0:
                a = i + 1
            else:
                b = i + 1
            if s[i].find('#') == 0:
                c = 1
            else:
                c = s[i].find('#') + 1
            if s[i].rfind('#') == 9:
                d = 10
            else:
                d = s[i].rfind('#') + 1
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()
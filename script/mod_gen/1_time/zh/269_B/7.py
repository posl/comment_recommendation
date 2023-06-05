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
            a = i + 1
            b = i + 1
            c = s[i].find('#') + 1
            d = s[i].rfind('#') + 1
            break
    for i in range(a, 10):
        if s[i].find('#') != -1:
            b = i + 1
            break
    print(a, b)
    print(c, d)
main()

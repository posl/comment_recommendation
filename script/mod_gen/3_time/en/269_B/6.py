def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i].find('#') != -1:
            a = i
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            b = i
            break
    for i in range(10):
        if s[i].find('#') != -1:
            c = s[i].find('#')
            d = s[i].rfind('#')
            break
    print(str(a+1) + ' ' + str(b+1))
    print(str(c+1) + ' ' + str(d+1))

if __name__ == '__main__':
    main()
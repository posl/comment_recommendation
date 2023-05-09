def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i].count('#') == 0:
            continue
        if a == 0:
            a = i+1
            b = i+1
            c = s[i].index('#')+1
            d = s[i].rindex('#')+1
        else:
            b = i+1
            c = min(c, s[i].index('#')+1)
            d = max(d, s[i].rindex('#')+1)
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()
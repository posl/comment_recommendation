def main():
    s = input()
    l = len(s)
    c = 0
    for i in range(l):
        if i % 2 == 0:
            if s[i] == '1':
                c += 1
        else:
            if s[i] == '0':
                c += 1
    print(c if c < l - c else l - c)

if __name__ == '__main__':
    main()
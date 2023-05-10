def main():
    s = input()
    l = len(s)
    v = 0
    w = 0
    for i in range(l):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
    print(v*w)

if __name__ == '__main__':
    main()
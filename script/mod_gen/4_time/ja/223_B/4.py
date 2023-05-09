def main():
    s = input()
    slen = len(s)
    smin = s
    smax = s
    for i in range(slen):
        s = s[1:] + s[0]
        if s < smin:
            smin = s
        if s > smax:
            smax = s
    print(smin)
    print(smax)

if __name__ == '__main__':
    main()
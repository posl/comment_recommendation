def main():
    s = input()
    n = len(s)
    smin = s
    smax = s
    for i in range(n):
        s = s[1:] + s[0]
        smin = min(s,smin)
        smax = max(s,smax)
    print(smin)
    print(smax)

if __name__ == '__main__':
    main()
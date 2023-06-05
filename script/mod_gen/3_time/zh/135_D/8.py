def main():
    s = input()
    s = s[::-1]
    d = [0] * 13
    d[0] = 1
    m = 1
    for i in range(len(s)):
        if s[i] == "?":
            d2 = [0] * 13
            for j in range(10):
                for k in range(13):
                    d2[(k + j * m) % 13] += d[k]
                    d2[(k + j * m) % 13] %= 1000000007
            d = d2
        else:
            d2 = [0] * 13
            for k in range(13):
                d2[(k + int(s[i]) * m) % 13] += d[k]
                d2[(k + int(s[i]) * m) % 13] %= 1000000007
            d = d2
        m = (m * 10) % 13
    print(d[5])

if __name__ == '__main__':
    main()
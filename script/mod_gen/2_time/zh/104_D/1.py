def main():
    s = input()
    q = s.count("?")
    abc = 0
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == "A":
            abc += b * (3 ** q)
            abc %= 1000000007
            a += (3 ** q)
            a %= 1000000007
        elif s[i] == "B":
            b += a
            b %= 1000000007
        elif s[i] == "C":
            pass
        else:
            abc *= 3
            abc %= 1000000007
            b *= 3
            b %= 1000000007
            a *= 3
            a %= 1000000007
            q -= 1
    print(abc)

if __name__ == '__main__':
    main()
def count_comma(n):
    if n <= 999:
        return 0
    else:
        s = str(n)
        l = len(s)
        if l % 3 == 0:
            return (l // 3 - 1) * 2 + count_comma(int(s[3:]))
        else:
            return (l // 3) * 2 + count_comma(int(s[l % 3:]))

if __name__ == '__main__':
    count_comma()
def count_comma(n):
    s = str(n)
    l = len(s)
    if l < 4:
        return 0
    elif l < 7:
        return int(s[:l-3]) - 1
    elif l < 10:
        return int(s[:l-6]) + 999999
    elif l < 13:
        return int(s[:l-9]) + 1999998
    elif l < 16:
        return int(s[:l-12]) + 2999997
    else:
        return 2999997 + 9000000 * (int(s[0]) - 2)
n = int(input())
print(count_comma(n))

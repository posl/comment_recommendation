def convert(s):
    n = len(s)
    if n == 1:
        return ord(s) - 65 + 1
    else:
        return 26 * (n - 1) + convert(s[:-1]) * 26 + ord(s[-1]) - 65 + 1
print(convert(input()))

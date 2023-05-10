def get_number(s, c, n):
    x = 0
    for i in range(len(s)):
        if s[i] == c:
            x += (10 ** (len(s) - i - 1)) * n
    return x
s1 = input()
s2 = input()
s3 = input()
s = set(s1 + s2 + s3)

if __name__ == '__main__':
    get_number()
def is_valid_month(m):
    return 1 <= m and m <= 12
s = input()
a = int(s[:2])
b = int(s[2:])

if __name__ == '__main__':
    is_valid_month()
def is_month(s):
    return 1 <= int(s) <= 12
s = input()
a = s[:2]
b = s[2:]

if __name__ == '__main__':
    is_month()
def main():
    s = input()
    n = len(s)
    if n == 1:
        if s == '8':
            print('是')
        else:
            print('否')
        return
    if n == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    if n == 3:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0 or int(s[2] + s[1] + s[0]) % 8 == 0 or int(s[1] + s[0] + s[2]) % 8 == 0:
            print('是')
        else:
            print('否')
        return
    if n == 4:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 or int(s[1] + s[2] + s[3]) % 8 == 0 or int(s[2] + s[3] + s[1]) % 8 == 0 or int(s[3] + s[1] + s[2]) % 8 == 0 or int(s[3] + s[2] + s[1]) % 8 == 0 or int(s[2] + s[1] + s[3]) % 8 == 0 or int(s[1] + s[3] + s[2]) % 8 == 0 or int(s[0] + s[2] + s[1] + s[3]) % 8 == 0 or int(s[0] + s[1] + s[3] + s[2]) % 8 == 0 or int(s[0] + s[3] + s[2] + s[1]) % 8 == 0 or int(s[0] + s[3] + s[1] + s[2]) % 8 == 0 or int(s[0

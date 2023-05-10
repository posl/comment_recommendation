def main():
    s = input()
    s = s[::-1]
    r = 0
    b = 0
    for i in range(len(s)):
        if s[i] == '0':
            r += 1
        else:
            b += 1
        if r == b:
            print(r+b)
            return
    print(0)

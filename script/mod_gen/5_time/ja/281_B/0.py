def check(s):
    if s[0].isupper() and s[-1].isupper():
        s = s[1:-1]
        if s.isdecimal() and int(s) >= 100000 and int(s) <= 999999:
            return True
    return False
s = input()
print("Yes" if check(s) else "No")

if __name__ == '__main__':
    check()
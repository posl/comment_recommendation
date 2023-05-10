def check(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
n = len(s)

if __name__ == '__main__':
    check()
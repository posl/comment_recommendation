def check(s, t):
    if not len(s) + 1 == len(t):
        return False
    if not t.startswith(s):
        return False
    return True
s = input()
t = input()

if __name__ == '__main__':
    check()
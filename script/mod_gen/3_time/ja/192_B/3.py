def check(s):
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        return True
    else:
        return False

if __name__ == '__main__':
    check()
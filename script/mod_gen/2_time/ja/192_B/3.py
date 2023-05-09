def check(s):
    odd = s[::2]
    even = s[1::2]
    return odd.islower() and even.isupper()
s = input()
print('Yes' if check(s) else 'No')

if __name__ == '__main__':
    check()
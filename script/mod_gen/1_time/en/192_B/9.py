def is_hard_to_read(s):
    odd = s[::2]
    even = s[1::2]
    return odd.islower() and even.isupper()
s = input()

if __name__ == '__main__':
    is_hard_to_read()
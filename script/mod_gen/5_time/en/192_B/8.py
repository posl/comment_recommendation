def is_hard_to_read(s):
    even = s[::2]
    odd = s[1::2]
    return even.isupper() and odd.islower()
s = input()
print('Yes' if is_hard_to_read(s) else 'No')

if __name__ == '__main__':
    is_hard_to_read()
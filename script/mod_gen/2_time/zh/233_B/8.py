def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = reversed(s[l-1:r])
    return ''.join(s)

if __name__ == '__main__':
    reverse_string()
def reverse_string(s, l, r):
    s = list(s)
    s[l-1:r] = s[l-1:r][::-1]
    s = ''.join(s)
    return s

if __name__ == '__main__':
    reverse_string()
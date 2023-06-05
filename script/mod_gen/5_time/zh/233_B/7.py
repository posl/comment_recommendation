def reverse_string(s, l, r):
    s = list(s)
    for i in range(l-1, r):
        s[i] = s[r - i + l - 2]
    return ''.join(s)

if __name__ == '__main__':
    reverse_string()
def swap_char(s, a, b):
    s = list(s)
    tmp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = tmp
    return ''.join(s)

if __name__ == '__main__':
    swap_char()
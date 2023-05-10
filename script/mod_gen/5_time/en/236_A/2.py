def swap_char(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

if __name__ == '__main__':
    swap_char()
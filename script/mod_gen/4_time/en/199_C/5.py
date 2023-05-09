def swap(s, a, b):
    if a == b:
        return s
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

if __name__ == '__main__':
    swap()
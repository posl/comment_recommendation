def swap(s,a,b):
    s = s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    return s

if __name__ == '__main__':
    swap()
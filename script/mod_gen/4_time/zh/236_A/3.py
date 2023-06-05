def swap(s, a, b):
    s1 = s[:a-1]
    s2 = s[a-1]
    s3 = s[a:b-1]
    s4 = s[b-1]
    s5 = s[b:]
    return s1+s4+s3+s2+s5

if __name__ == '__main__':
    swap()
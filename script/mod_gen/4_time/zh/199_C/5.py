def swap(s, a, b):
    temp = s[a-1]
    s[a-1] = s[b-1]
    s[b-1] = temp

if __name__ == '__main__':
    swap()
def swap(s, i, j):
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

if __name__ == '__main__':
    swap()
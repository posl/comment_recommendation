def reverse_str(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

if __name__ == '__main__':
    reverse_str()
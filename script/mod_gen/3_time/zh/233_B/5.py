def reverse_str(s, l, r):
    if l < 1 or r > len(s):
        return s
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

if __name__ == '__main__':
    reverse_str()
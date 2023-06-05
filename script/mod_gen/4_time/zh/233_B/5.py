def reverse_string(s, l, r):
    if l == 1:
        return s[r-1::-1] + s[r:]
    else:
        return s[:l-1] + s[r-1:l-2:-1] + s[r:]

if __name__ == '__main__':
    reverse_string()
def reverse_string(s, l, r):
    if l > r:
        return s
    else:
        s = s[:l-1] + s[r-1:l-2:-1] + s[r:]
        return s

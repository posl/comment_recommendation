def reverse_str(s, l, r):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

def reverse(l, r, s):
    return s[:l-1] + s[l-1:r][::-1] + s[r:]

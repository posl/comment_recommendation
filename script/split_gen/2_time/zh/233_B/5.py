def reverse_string(s, L, R):
    s = s[:L-1] + s[L-1:R][::-1] + s[R:]
    return s

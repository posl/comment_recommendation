def reverse(s, L, R):
    return s[:L-1] + s[L-1:R][::-1] + s[R:]

if __name__ == '__main__':
    reverse()
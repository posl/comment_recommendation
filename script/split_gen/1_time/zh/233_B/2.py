def reverse(s, L, R):
    s = list(s)
    if L == 1:
        return ''.join(list(reversed(s[L-1:R]))) + ''.join(s[R:])
    else:
        return ''.join(s[:L-1]) + ''.join(list(reversed(s[L-1:R]))) + ''.join(s[R:])

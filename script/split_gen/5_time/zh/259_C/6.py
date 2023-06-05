def is_subsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)
s = input()
t = input()

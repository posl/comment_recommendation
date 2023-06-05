def is_subsequence(s, t):
    t = iter(t)
    return all(c in t for c in s)
s = input()
t = input()

if __name__ == '__main__':
    is_subsequence()
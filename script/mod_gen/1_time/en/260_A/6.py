def find_unique(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return -1
s = input()
print(find_unique(s))

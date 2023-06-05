def move(s):
    s = list(s)
    s.append(s[0])
    s.pop(0)
    s = "".join(s)
    return s
s = input()
print(move(s))

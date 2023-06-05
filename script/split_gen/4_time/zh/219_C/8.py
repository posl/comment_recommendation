def compare(s1, s2, x):
    if len(s1) < len(s2):
        s1 = s1 + 'a' * (len(s2) - len(s1))
    elif len(s1) > len(s2):
        s2 = s2 + 'a' * (len(s1) - len(s2))
    for i in range(len(s1)):
        if x.index(s1[i]) < x.index(s2[i]):
            return -1
        elif x.index(s1[i]) > x.index(s2[i]):
            return 1
    return 0
x = input()
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort(cmp=lambda s1, s2:compare(s1, s2, x))
for i in range(n):
    print s[i]

def flip(s):
    n = len(s)
    s1 = s[:n//2]
    s2 = s[n//2:]
    return s2 + s1
n = int(input())
s = input()
q = int(input())
for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a-1, b-1
    if t == 1:
        s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else:
        s = flip(s)
print(s)

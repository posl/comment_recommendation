def next_permutation(s):
    i = len(s) - 1
    while i > 0 and s[i-1] >= s[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(s) - 1
    while s[j] <= s[i-1]:
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return True
s, k = input().split()
s = list(s)
k = int(k)
for i in range(k):
    next_permutation(s)
print(''.join(s))

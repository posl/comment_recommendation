def permutation(s, k):
    if len(s) <= 1:
        return s
    else:
        c = s[0]
        s = s[1:]
        l = []
        for i in range(len(s) + 1):
            l.append(c + permutation(s[:i] + s[i:], k))
        l.sort()
        return l[k-1]
s, k = input().split()
print(permutation(s, int(k)))

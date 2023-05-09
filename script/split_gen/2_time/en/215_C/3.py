def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                res.append(s[i] + p)
        return res
s, k = input().split()
k = int(k)
print(sorted(permutations(s))[k-1])

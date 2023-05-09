def permute(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                yield s[i] + p
s, k = input().split()
k = int(k)
s = sorted(list(set(permute(s))))
print(s[k-1])

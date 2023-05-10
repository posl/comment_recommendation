def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        p = []
        for i in range(len(s)):
            p += [s[i] + x for x in permutation(s[:i] + s[i+1:])]
        return p
s, k = input().split()
k = int(k)
p = permutation(s)
p.sort()
print(p[k-1])

if __name__ == '__main__':
    permutation()
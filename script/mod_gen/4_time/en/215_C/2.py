def permutation(s):
    if len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[::-1]]
    else:
        l = []
        for i in range(len(s)):
            p = permutation(s[:i] + s[i + 1:])
            for x in p:
                l.append(s[i] + x)
        return l
S, K = input().split()
K = int(K)
S = list(S)
S.sort()
S = "".join(S)
p = permutation(S)
p = list(set(p))
p.sort()
print(p[K - 1])

if __name__ == '__main__':
    permutation()
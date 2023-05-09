def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            perms += [s[i] + p for p in permute(s[:i] + s[i+1:])]
        return perms
S, K = input().split()
K = int(K)
perms = permute(S)
perms.sort()
print(perms[K-1])

if __name__ == '__main__':
    permute()
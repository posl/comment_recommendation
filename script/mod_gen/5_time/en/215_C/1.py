def permute(s):
    if len(s) <= 1:
        return [s]
    perms = permute(s[1:])
    char = s[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
s, k = map(str, input().split())
k = int(k)
perms = permute(s)
perms.sort()
print(perms[k-1])

if __name__ == '__main__':
    permute()
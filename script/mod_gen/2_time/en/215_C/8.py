def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perm = []
        for i in range(len(s)):
            x = s[i]
            xs = s[:i] + s[i+1:]
            for p in permute(xs):
                perm.append(x + p)
        return perm
s, k = input().split()
k = int(k)
perms = permute(s)
perms.sort()
print(perms[k-1])

if __name__ == '__main__':
    permute()
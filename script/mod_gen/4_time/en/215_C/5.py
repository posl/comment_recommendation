def permute(s, k):
    if len(s) == 1:
        return s
    else:
        res = []
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:], k):
                res.append(c + perm)
        return sorted(res)[k-1]
s, k = input().split()
print(permute(s, int(k)))

if __name__ == '__main__':
    permute()
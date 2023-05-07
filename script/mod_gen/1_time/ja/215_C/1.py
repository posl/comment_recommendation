def permute(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for j in permute(s[:i] + s[i+1:]):
                res.append(s[i] + j)
        return res
s, k = input().split()
k = int(k)
print(sorted(permute(s))[k-1])

if __name__ == '__main__':
    permute()
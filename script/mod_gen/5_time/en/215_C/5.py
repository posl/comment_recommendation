def permute(s, k):
    if len(s) == 1:
        return s
    else:
        l = []
        for i in range(len(s)):
            for j in permute(s[:i] + s[i+1:], k):
                l.append(s[i] + j)
        return l[k-1]
s, k = input().strip().split()
k = int(k)
s = ''.join(sorted(s))
print(permute(s, k))

if __name__ == '__main__':
    permute()
def xor(l):
    res = l[0]
    for i in range(1, len(l)):
        res = res ^ l[i]
    return res
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(2 ** (2 * n)):
    tmp = []
    for j in range(2 * n):
        if ((i >> j) & 1):
            tmp.append(j)
    if (len(tmp) == n * 2):
        tmp2 = []
        for j in range(n):
            tmp2.append(a[tmp[2 * j]][tmp[2 * j + 1]])
        ans = max(ans, xor(tmp2))
print(ans)

if __name__ == '__main__':
    xor()
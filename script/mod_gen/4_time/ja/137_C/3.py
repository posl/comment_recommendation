def count(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d
N = int(input())
s = [input() for _ in range(N)]
d = [count(s[i]) for i in range(N)]
print(d)
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if d[i] == d[j]:
            ans += 1
print(ans)

if __name__ == '__main__':
    count()
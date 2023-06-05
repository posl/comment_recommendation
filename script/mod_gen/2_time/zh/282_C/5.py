def solve(n, m, s):
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            for k in range(m):
                if s[i - 1][k] == 'o' or s[j - 1][k] == 'o':
                    if k == m - 1:
                        count += 1
                else:
                    break
    return count
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
print(solve(n, m, s))

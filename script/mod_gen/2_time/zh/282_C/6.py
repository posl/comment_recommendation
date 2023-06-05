def solve(n, m, s):
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    if k == m-1:
                        ans += 1
                else:
                    break
    return ans
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
print(solve(n, m, s))

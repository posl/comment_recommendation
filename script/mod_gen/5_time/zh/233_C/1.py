def solve(n, x, L, a):
    ans = 0
    # write your code here
    return ans
n, x = map(int, input().split())
L = []
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    a.append(tmp[1:])
ans = solve(n, x, L, a)
print(ans)

if __name__ == '__main__':
    solve()
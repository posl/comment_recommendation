def solve(n, p):
    max = 0
    cnt = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
            cnt += 1
    return cnt
n = int(input())
p = list(map(int, input().split()))
print(solve(n, p))

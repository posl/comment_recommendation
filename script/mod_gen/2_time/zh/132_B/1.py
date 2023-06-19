def solve():
    n = int(input())
    p = [int(i) for i in input().split()]
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    return cnt
print(solve())

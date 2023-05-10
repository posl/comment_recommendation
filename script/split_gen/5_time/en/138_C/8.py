def solve(N, v):
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1])/2
    return v[N-1]
N = int(input())
v = list(map(int, input().split()))
print(solve(N, v))

def solve(n, h):
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            return False
    return True
n = int(input())
h = list(map(int, input().split()))

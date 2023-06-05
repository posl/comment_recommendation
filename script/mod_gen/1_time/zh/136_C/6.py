def solve(n, h):
    for i in range(n-1):
        if h[i+1] > h[i]:
            h[i+1] -= 1
        elif h[i+1] < h[i]:
            return False
    return True
n = int(input())
h = list(map(int, input().split()))
print('Yes' if solve(n, h) else 'No')

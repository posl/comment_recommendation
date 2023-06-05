def solve(n, h):
    ans = 0
    while True:
        left = -1
        right = -1
        for i in range(n):
            if h[i] > 0:
                if left == -1:
                    left = i
                right = i
        if left == -1:
            break
        for i in range(left, right+1):
            h[i] -= 1
        ans += 1
    return ans
n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))

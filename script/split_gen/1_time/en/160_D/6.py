def solve(n, x, y):
    ans = [0] * n
    for i in range(1, n):
        for j in range(i+1, n+1):
            ans[min(j-i, abs(x-i)+1+abs(y-j), abs(y-i)+1+abs(x-j))-1] += 1
    return ans

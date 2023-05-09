def main():
    x, y, n = map(int, input().split())
    ans = 10**9
    for i in range(0, n+1):
        for j in range(0, n+1):
            if i*3 + j > n:
                break
            if i*3 + j == n:
                ans = min(ans, i*x + j*y)
    print(ans)

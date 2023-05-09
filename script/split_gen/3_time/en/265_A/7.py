def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(0, n+1):
        ans = min(ans, n*i*x + (n-i)//3*y)
    print(ans)

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j <= n and i == j and i * j == int((i * j)**0.5)**2:
                ans += 1
            elif i * j <= n and i * j == int((i * j)**0.5)**2:
                ans += 2
    print(ans)

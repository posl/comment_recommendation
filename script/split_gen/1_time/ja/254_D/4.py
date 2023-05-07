def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                if i == j:
                    ans += 1
                else:
                    ans += 2
    print(ans)

def main():
    n = int(input())
    ans = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a * b * c <= n:
                    ans += 1
                else:
                    break
    print(ans)

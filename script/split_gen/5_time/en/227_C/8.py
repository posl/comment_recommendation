def main():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            if b > n / a:
                break
            ans += int(n / a / b)
    print(ans)

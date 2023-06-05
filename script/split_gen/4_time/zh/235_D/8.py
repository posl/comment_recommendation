def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0: n //= a
        elif n % 10 == 1: n = (n - 1) // 10
        else:
            print(-1)
            return
        ans += 1
    print(ans)

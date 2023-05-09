def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        ans += 1
        if n % a == 0:
            n //= a
        else:
            n -= 1
        if n % a != 0 and n != 1:
            print(-1)
            return
    print(ans)

def main():
    a, n = map(int, input().split())
    if a == 10:
        if n == 10:
            print(1)
        else:
            print(-1)
        return
    if n == a:
        print(2)
        return
    if n < a:
        print(-1)
        return
    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

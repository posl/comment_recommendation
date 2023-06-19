def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % 10 == 0:
            n //= 10
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)
main()

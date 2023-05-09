def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % a == 1:
            n -= 1
            ans += 1
        else:
            print(-1)
            exit()
    print(ans)

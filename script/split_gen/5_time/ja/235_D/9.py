def main():
    a, n = map(int, input().split())
    ans = 0
    while n != 1:
        if n % a != 0:
            n -= 1
            ans += 1
        elif n % a == 0:
            n /= a
            ans += 1
        if n == 0:
            print(-1)
            exit()
    print(ans)

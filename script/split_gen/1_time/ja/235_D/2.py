def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 != 0:
            n = int(str(n % 10) + str(n // 10))
        else:
            ans = -1
            break
        ans += 1
    print(ans)

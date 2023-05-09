def main():
    a, n = map(int, input().split())
    ans = 0
    while n != 1:
        if n % a == 0:
            n //= a
            ans += 1
        else:
            if len(str(n)) == 1:
                print(-1)
                return
            n = int(str(n)[-1] + str(n)[:-1])
            ans += 1
    print(ans)

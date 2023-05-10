def main():
    n = int(input())
    ans = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

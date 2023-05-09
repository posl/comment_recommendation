def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        exit(0)
    if a == 1:
        print(1)
        exit(0)
    cnt = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        cnt += 1
    print(cnt)
    exit(0)

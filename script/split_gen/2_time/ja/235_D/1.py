def main():
    a, n = map(int, input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 != 0:
            n = int(str(n % 10) + str(n // 10))
        else:
            break
        count += 1
    if n == 1:
        print(count)
    else:
        print(-1)

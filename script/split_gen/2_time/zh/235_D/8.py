def main():
    a, n = map(int, input().split())
    cnt = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        cnt += 1
    print(cnt)

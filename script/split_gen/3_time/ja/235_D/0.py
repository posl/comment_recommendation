def main():
    a, n = map(int, input().split())
    cnt = 0
    while n > 1:
        if n % a == 0:
            n //= a
            cnt += 1
        elif n % 10 == 0:
            n //= 10
            cnt += 1
        else:
            print(-1)
            return
    print(cnt)

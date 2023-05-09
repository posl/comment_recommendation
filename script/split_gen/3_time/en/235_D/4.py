def main():
    a, n = map(int, input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            if n % 10 == 0:
                n //= 10
            else:
                print(-1)
                exit()
        count += 1
    print(count)

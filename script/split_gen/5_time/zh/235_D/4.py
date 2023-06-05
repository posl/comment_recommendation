def main():
    a, n = map(int, input().split())
    c = 0
    while n > 1:
        if n % a == 0:
            n = n // a
        else:
            n -= 1
        c += 1
    print(c)

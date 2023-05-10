def main():
    n, a, b = map(int, input().split())
    if a + b == 0:
        print(0)
    elif a == 0:
        print(n)
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))

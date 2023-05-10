def main():
    n, a, b = map(int, input().split())
    q, mod = divmod(n, a + b)
    print(q * a + min(a, mod))

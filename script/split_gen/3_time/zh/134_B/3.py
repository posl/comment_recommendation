def main():
    n,d = map(int,input().split())
    print(2 if n % (2 * d + 1) == 0 else n // (2 * d + 1) + 1)

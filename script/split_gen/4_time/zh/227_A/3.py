def main():
    n,k,a = map(int, input().split())
    a = a - 1
    print((k - 1 + a) % n + 1)

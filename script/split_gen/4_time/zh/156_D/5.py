def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if b - a == 1:
        print(n*(n-1) % (10**9+7))
    else:
        print((n-a-b+1)*(n-a-b+2) % (10**9+7))

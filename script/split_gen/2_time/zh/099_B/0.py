def main():
    a, b = map(int, input().split())
    n = b - a
    print(int(n*(n-1)/2 - a))

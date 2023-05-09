def main():
    n, k, a = map(int, input().split())
    print((k-1+a-1)%n+1)

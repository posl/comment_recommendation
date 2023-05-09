def main():
    n,k = map(int, input().split())
    n %= k
    print(min(n, abs(n-k)))

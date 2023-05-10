def main():
    n, k = map(int, input().split())
    while n >= k:
        n = n % k
        n = abs(n-k)
    print(n)

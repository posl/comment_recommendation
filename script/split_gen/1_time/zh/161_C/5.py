def main():
    n, k = map(int, input().split())
    while n >= k:
        n = n % k
        if n == 0:
            print(0)
            return
    print(min(n, abs(k - n)))

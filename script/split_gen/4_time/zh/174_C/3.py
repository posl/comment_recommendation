def main():
    k = int(input())
    n = 1
    while n <= k:
        if n % k == 0:
            print(n)
            return
        n = n * 10 + 1
    print(-1)

def main():
    n, k = map(int, input().split())
    i = 0
    while n > 0:
        n //= k
        i += 1
    print(i)

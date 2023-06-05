def main():
    n, k = map(int, input().split())
    count = 0
    while n >= k:
        count += 1
        n //= k
    print(count + 1)
main()

def main():
    n, k, x = map(int, input().split())
    items = list(map(int, input().split()))
    items.sort()
    total = 0
    for item in items[:-k]:
        total += item
    total += k * x
    print(total)

if __name__ == '__main__':
    main()
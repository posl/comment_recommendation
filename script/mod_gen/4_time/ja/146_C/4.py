def main():
    a, b, x = map(int, input().split())
    result = 0
    for d in range(1, 10):
        n = (x - b * d) // a
        if n > 0 and len(str(n)) == d:
            result = n if result < n else result
    print(result)

if __name__ == '__main__':
    main()
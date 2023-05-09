def main():
    n, k = map(int, input().split())
    result = 0
    for i in range(1, n+1):
        if i >= k:
            result += 1/n
            continue
        count = 0
        while i < k:
            i *= 2
            count += 1
        result += (1/n) * (1/(2**count))
    print(result)

if __name__ == '__main__':
    main()
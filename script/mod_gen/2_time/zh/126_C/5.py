def main():
    n, k = map(int, input().split())
    res = 0
    for i in range(1, n + 1):
        if i >= k:
            res += 1 / n
        else:
            res += 1 / n * (1 / 2) ** (k - i).bit_length()
    print(res)

if __name__ == '__main__':
    main()
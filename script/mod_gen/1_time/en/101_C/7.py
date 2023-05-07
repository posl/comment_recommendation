def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_a = min(a)
    min_a_idx = a.index(min_a)
    if min_a_idx < k:
        print(1 + ((n - k) // (k - 1) + ((n - k) % (k - 1) != 0)))
    else:
        print(1 + ((n - k) // (k - 1) + ((n - k) % (k - 1) != 0)) + ((min_a_idx - k) // (k - 1) + ((min_a_idx - k) % (k - 1) != 0)))

if __name__ == '__main__':
    main()
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    result = 0
    for i in range(1, 41):
        mask = 1 << (40 - i)
        count = 0
        for j in range(n):
            if a[j] & mask:
                count += 1
        if count <= n // 2 and result + mask <= k:
            result += mask
    s = 0
    for i in range(n):
        s += result ^ a[i]
    print(s)

if __name__ == '__main__':
    main()
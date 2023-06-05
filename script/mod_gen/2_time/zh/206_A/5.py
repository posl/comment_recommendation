def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    i = 0
    j = 0
    while i < q:
        if j < n:
            if k[i] == a[j]:
                j += 1
            else:
                k[i] -= j
                i += 1
        else:
            k[i] -= j
            i += 1
    for i in k:
        print(i)

if __name__ == '__main__':
    main()
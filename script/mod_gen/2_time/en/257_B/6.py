def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
        if a[l[i] - 1] > n:
            a[l[i] - 1] = 1
        for j in range(k):
            if j != l[i] - 1:
                if a[j] == a[l[i] - 1]:
                    a[j] += 1
                    if a[j] > n:
                        a[j] = 1
    for i in range(k):
        print(a[i], end=' ')
    print()

if __name__ == '__main__':
    main()
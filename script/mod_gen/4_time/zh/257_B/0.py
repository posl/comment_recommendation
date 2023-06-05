def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i] - 1] += 1
    for i in range(q):
        for j in range(k):
            if b[a[l[j] - 1] - 1] == 0:
                a[l[j] - 1] += 1
                b[a[l[j] - 1] - 1] += 1
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
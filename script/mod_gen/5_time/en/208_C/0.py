def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [k // n] * n
    k %= n
    for i in range(k):
        b[i] += 1
    for i in range(n):
        print(b[a.index(a[i])])

if __name__ == '__main__':
    main()
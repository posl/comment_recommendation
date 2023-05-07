def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    c = k // n
    k %= n
    for i in range(n):
        b[i] = c
    d = sorted(a)
    for i in range(k):
        b[a.index(d[i])] += 1
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    main()
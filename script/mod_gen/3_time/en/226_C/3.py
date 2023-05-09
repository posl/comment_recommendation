def main():
    n = int(input())
    t = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i], k, *a = map(int, input().split())
        for j in range(k):
            t[i] = max(t[i], t[a[j]] + 1)
    print(t[n])

if __name__ == '__main__':
    main()
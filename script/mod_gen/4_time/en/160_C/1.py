def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_dist = 0
    for i in range(n - 1):
        max_dist = max(max_dist, a[i + 1] - a[i])
    max_dist = max(max_dist, k - a[n - 1] + a[0])
    print(k - max_dist)

if __name__ == '__main__':
    main()
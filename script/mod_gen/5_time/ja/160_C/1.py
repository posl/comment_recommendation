def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_distance = 0
    for i in range(n):
        if i == n - 1:
            distance = k - a[i] + a[0]
        else:
            distance = a[i + 1] - a[i]
        if distance > max_distance:
            max_distance = distance
    print(k - max_distance)

if __name__ == '__main__':
    main()
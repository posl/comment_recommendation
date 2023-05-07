def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_distance = 0
    for i in range(n-1):
        if max_distance < a[i+1]-a[i]:
            max_distance = a[i+1]-a[i]
    if max_distance < k - a[-1] + a[0]:
        max_distance = k - a[-1] + a[0]
    print(k-max_distance)

if __name__ == '__main__':
    main()
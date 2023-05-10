def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(k)
    a.append(a[0] + k)
    a.sort()
    max = 0
    for i in range(n):
        if a[i+1] - a[i] > max:
            max = a[i+1] - a[i]
    print(k - max)

if __name__ == '__main__':
    main()
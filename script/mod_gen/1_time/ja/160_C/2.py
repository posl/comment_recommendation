def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if i == n-1:
            b.append(k - a[i] + a[0])
        else:
            b.append(a[i+1] - a[i])
    print(k - max(b))

if __name__ == '__main__':
    main()
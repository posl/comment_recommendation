def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0] + k)
    for i in range(n):
        a[i] = a[i+1] - a[i]
    print(k - max(a))

if __name__ == '__main__':
    main()
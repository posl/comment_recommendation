def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if total + a[i] > t:
            print(i+1, t-total)
            break
        total += a[i]
        if i == n-1:
            print(1, t-total)

if __name__ == '__main__':
    main()
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 1:
        print(n)
        return
    if n == k:
        print(1)
        return
    if a[0] == a[-1]:
        print(1)
        return
    if a[0] == a[k-1]:
        print(n - k + 1)
        return
    if a[k-1] == a[k]:
        print(n - k + 1)
        return
    if a[k-1] < a[k]:
        print(1)
        return
    if a[k-1] > a[k]:
        print(2)
        return

if __name__ == '__main__':
    main()
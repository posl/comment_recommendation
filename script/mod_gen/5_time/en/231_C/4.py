def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        x = int(input())
        min = 0
        max = n
        while min < max:
            mid = (min + max) // 2
            if a[mid] < x:
                min = mid + 1
            else:
                max = mid
        print(n - min)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print("-1")
        return
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print("-1")
            return
    print(n - 1)

if __name__ == '__main__':
    main()
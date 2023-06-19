def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    print(sum(a))

if __name__ == '__main__':
    main()
def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0]>>1
        a.sort(reverse=True)
    print(sum(a))

if __name__ == '__main__':
    main()
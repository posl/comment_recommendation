def main():
    h, n = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()
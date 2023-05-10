def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n < m:
        print('No')
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[n - m + i] < b[i]:
                print('No')
                break
        else:
            print('Yes')

if __name__ == '__main__':
    main()
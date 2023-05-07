def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    for i in range(n - k):
        if a[i] > b[i + k]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
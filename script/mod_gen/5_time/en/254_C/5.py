def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        print('Yes')
        return
    for i in range(n-k):
        if a[i] > a[i+k]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
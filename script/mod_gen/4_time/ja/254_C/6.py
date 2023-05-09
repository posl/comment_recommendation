def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if (a[-1] - a[0] <= k):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
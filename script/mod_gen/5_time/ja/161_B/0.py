def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    for i in range(m):
        if a[i] < s / (4 * m):
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()
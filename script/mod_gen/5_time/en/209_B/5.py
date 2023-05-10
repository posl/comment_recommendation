def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a[i] for i in range(n) if i % 2 == 0]
    if sum(a) <= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
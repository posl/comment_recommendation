def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            a[i] -= 1
        sum += a[i]
    if sum <= x:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()
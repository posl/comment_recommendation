def main():
    n,m = input().split()
    n = int(n)
    m = int(m)
    a = input().split()
    a = [int(i) for i in a]
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum <= n:
        print(n-sum)
    else:
        print(-1)

if __name__ == '__main__':
    main()
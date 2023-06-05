def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    sum = 0
    for i in range(n):
        if i < l:
            sum += a[i]
        else:
            sum += a[l-1]
    print(sum)

if __name__ == '__main__':
    main()
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(k):
        if n >= a[i]:
            n -= a[i]
            count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    main()
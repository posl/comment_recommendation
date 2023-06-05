def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += a[j]
            if tmp == k:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
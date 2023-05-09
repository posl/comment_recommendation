def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            elif a[i] % 3 == 0:
                a[i] = a[i] // 3
            else:
                if i == n-1:
                    print(-1)
                    return
                else:
                    continue
        cnt += 1
        if len(set(a)) == 1:
            print(cnt)
            return

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] > n:
                continue
            if a[a[i]//a[j]] == 0:
                continue
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - 1 for i in range(n)]
    cnt = 0
    for i in range(n):
        if i == a[a[i]]:
            cnt += 1
    if cnt == n:
        print(0)
        exit()
    for i in range(n):
        if i == a[a[i]]:
            cnt -= 1
        if i == a[i]:
            cnt += 1
    print(cnt // 2)

if __name__ == '__main__':
    main()
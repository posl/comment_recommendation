def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                cnt += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                cnt += 1
        else:
            if a[i] != a[i-1] and a[i] != a[i+1]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
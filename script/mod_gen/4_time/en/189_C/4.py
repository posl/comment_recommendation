def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        cnt = 0
        for i in range(n):
            if cnt == 0:
                if a[i] >= x:
                    cnt += 1
            else:
                if a[i] >= x:
                    cnt += 1
                else:
                    ans = max(ans, cnt*x)
                    cnt = 0
        ans = max(ans, cnt*x)
    print(ans)

if __name__ == '__main__':
    main()
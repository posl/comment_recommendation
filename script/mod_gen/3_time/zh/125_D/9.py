def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - abs(min(a)) * 2)

if __name__ == '__main__':
    main()
def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    num = 0
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[i] = k//n
    for i in range(n):
        if ans[i] > a[i]:
            num += ans[i] - a[i]
    for i in range(n):
        if num == 0:
            break
        if ans[i] > a[i]:
            if num > 0:
                ans[i] -= 1
                num -= 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if i != 0 and a[i-1] != a[i]:
            ans[cnt] += 1
            cnt = 0
        else:
            cnt += 1
    ans[cnt] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
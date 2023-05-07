def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    cnt = 0
    ans = [0] * n
    for i in range(n):
        cnt += 1
        if a[i] != a[i+1]:
            ans[cnt-1] += 1
            cnt = 0
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
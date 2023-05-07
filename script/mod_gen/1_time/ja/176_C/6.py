def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, -1, -1):
        if a[i] > ans:
            ans = a[i]
        else:
            ans = a[i] - 1
        if ans < 0:
            print(-1)
            return
    print(sum(a) - n)

if __name__ == '__main__':
    main()
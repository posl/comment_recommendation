def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i == j:
                continue
            tmp += a[j]
        ans = max(ans, min(tmp, 360-tmp))
    print(ans)

if __name__ == '__main__':
    main()
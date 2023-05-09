def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        ans = min(ans + a[i-1], a[i])
    print(ans)

if __name__ == '__main__':
    main()
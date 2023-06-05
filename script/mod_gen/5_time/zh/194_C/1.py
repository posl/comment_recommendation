def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        for j in range(i):
            ans += (a[i] - a[j]) ** 2
    print(ans)

if __name__ == '__main__':
    main()
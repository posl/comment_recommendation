def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] - a[j]) % 200 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
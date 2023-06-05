def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if i in a[j][1:]:
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()
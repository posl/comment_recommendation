def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        if a[i - 1] < i:
            continue
        for j in range(i + 1, n + 1):
            if a[j - 1] < j:
                continue
            if a[i - 1] == i and a[j - 1] == j:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = {}
    for i in range(n):
        if a[i] in count:
            count[a[i]] += 1
        else:
            count[a[i]] = 1
    ans = 0
    for i in count:
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()
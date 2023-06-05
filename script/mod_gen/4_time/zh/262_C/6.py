def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    ans = 0
    for i in range(1, n + 1):
        if b[i] == i:
            ans += 1
    for i in range(1, n + 1):
        if b[i] != i:
            if b[b[i]] == i:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
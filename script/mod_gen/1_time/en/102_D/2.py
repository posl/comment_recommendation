def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    ans = float('inf')
    for i in range(1, n):
        for j in range(i + 1, n):
            x = s[i]
            y = s[j] - s[i]
            z = s[n] - s[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    j = 0
    ans = abs(a[0] - b[0])
    for i in range(n):
        while j < m - 1 and abs(a[i] - b[j + 1]) < abs(a[i] - b[j]):
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

if __name__ == '__main__':
    main()
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = float('inf')
    i = 0
    for x in a:
        while i < m and b[i] < x:
            i += 1
        if i < m:
            ans = min(ans, b[i] - x)
        if i > 0:
            ans = min(ans, x - b[i-1])
    print(ans)

if __name__ == '__main__':
    main()
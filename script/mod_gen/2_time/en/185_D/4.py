def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a + [n + 1]
    a.sort()
    b = []
    for i in range(m + 1):
        b.append(a[i + 1] - a[i] - 1)
    b = [x for x in b if x > 0]
    k = min(b)
    ans = 0
    for x in b:
        ans += (x + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()
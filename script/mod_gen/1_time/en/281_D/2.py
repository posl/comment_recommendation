def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            s.add(a[i] + a[j])
    ans = -1
    for i in s:
        if i % d == 0:
            ans = max(ans, i)
    print(ans)
main()

if __name__ == '__main__':
    main()
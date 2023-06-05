def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = [0]
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                s.append(a[i] + a[j] + a[k])
    s.sort()
    s = list(set(s))
    ans = 0
    for i in range(len(s)):
        if s[i] <= w:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
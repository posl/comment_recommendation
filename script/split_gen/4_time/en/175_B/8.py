def triangle():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n - 2):
        a = l[i]
        for j in range(i + 1, n - 1):
            b = l[j]
            for k in range(j + 1, n):
                c = l[k]
                if a + b > c and a != b and b != c:
                    ans += 1
    print(ans)
triangle()

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # print(n, q, a, k)
    a.sort()
    # print(a)
    b = [a[0] - 1]
    for i in range(1, n):
        b.append(a[i] - a[i - 1] - 1)
    b.append(10 ** 18 - a[-1])
    # print(b)
    c = [0]
    for i in range(n + 1):
        c.append(c[-1] + b[i])
    # print(c)
    for i in range(q):
        left = 0
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            if c[mid] >= k[i]:
                right = mid
            else:
                left = mid + 1
        print(a[left - 1] + (k[i] - c[left - 1]))

if __name__ == '__main__':
    solve()
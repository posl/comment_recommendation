def problem255_d():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    for i in range(n):
        a[i] -= i
    a.sort()
    ans = []
    for i in range(q):
        if x[i] > a[n - 1]:
            ans.append(x[i] - a[n - 1] + n)
        elif x[i] < a[0]:
            ans.append(a[0] - x[i])
        else:
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if a[mid] >= x[i]:
                    right = mid
                else:
                    left = mid + 1
            ans.append(a[right] - x[i] + n - right)
    for i in range(q):
        print(ans[i])
problem255_d()

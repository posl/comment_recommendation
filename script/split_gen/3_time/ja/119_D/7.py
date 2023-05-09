def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]
for i in range(q):
    ans = 10**18
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    for ss in [s[s_index - 1], s[s_index]]:
        for tt in [t[t_index - 1], t[t_index]]:
            d1 = abs(ss - x[i]) + abs(tt - ss)
            d2 = abs(tt - x[i]) + abs(ss - tt)
            ans = min(ans, d1, d2)
    print(ans)

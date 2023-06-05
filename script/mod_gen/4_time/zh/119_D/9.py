def binary_search(list1, x):
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = (left + right) // 2
        if list1[mid] == x:
            return mid
        elif list1[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
A, B, Q = map(int, input().split())
s = [int(input()) for i in range(A)]
t = [int(input()) for i in range(B)]
x = [int(input()) for i in range(Q)]
for i in range(Q):
    s_index = binary_search(s, x[i])
    t_index = binary_search(t, x[i])
    if s_index == 0:
        s_left = 0
    else:
        s_left = s[s_index - 1]
    if t_index == 0:
        t_left = 0
    else:
        t_left = t[t_index - 1]
    if s_index == A:
        s_right = 10 ** 10
    else:
        s_right = s[s_index]
    if t_index == B:
        t_right = 10 ** 10
    else:
        t_right = t[t_index]
    ans = 10 ** 10
    ans = min(ans, abs(x[i] - s_left) + abs(s_left - t_left))
    ans = min(ans, abs(x[i] - s_left) + abs(s_left - t_right))
    ans = min(ans, abs(x[i] - s_right) + abs(s_right - t_left))
    ans = min(ans, abs(x[i] - s_right) + abs(s_right - t_right))
    ans = min(ans, abs(x[i] - t_left) + abs(t_left - s_left))
    ans = min(ans, abs(x[i] - t_left) + abs(t_left - s_right))
    ans = min(ans, abs(x[i] - t_right) + abs(t_right - s_left))
    ans = min(ans, abs(x[i] - t_right) + abs(t_right - s_right))
    print(ans)

if __name__ == '__main__':
    binary_search()
def f(x, s, w):
    count = 0
    for i in range(len(s)):
        if s[i] == '0' and w[i] < x:
            count += 1
        elif s[i] == '1' and w[i] >= x:
            count += 1
    return count
n = int(input())
s = input()
w = [int(i) for i in input().split()]
max_w = max(w)
min_w = min(w)
max_x = max_w
min_x = min_w
max_f = f(max_x, s, w)
min_f = f(min_x, s, w)
while min_x < max_x:
    mid_x = (min_x + max_x) // 2
    mid_f = f(mid_x, s, w)
    if mid_f == max_f:
        min_x = mid_x
    elif mid_f == min_f:
        max_x = mid_x
    else:
        min_x = mid_x
        max_x = mid_x
print(max_f)

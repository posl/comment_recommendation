def get_min_distance(s,t,x):
    result = 0
    if len(s) == 0:
        return t[0] - x
    if len(t) == 0:
        return x - s[-1]
    if len(s) == 1 and len(t) == 1:
        return min(t[0] - x, x - s[-1])
    if x in s or x in t:
        return 0
    if x < s[0]:
        return s[0] - x
    if x > t[-1]:
        return x - t[-1]
    if x > s[-1] and x < t[0]:
        return min(x - s[-1], t[0] - x)
    if x > s[-1]:
        return x - s[-1]
    if x < t[0]:
        return t[0] - x
    left = 0
    right = len(s) - 1
    while left < right:
        mid = (left + right) // 2
        if s[mid] < x:
            left = mid + 1
        else:
            right = mid
    left = 0
    right = len(t) - 1
    while left < right:
        mid = (left + right) // 2
        if t[mid] < x:
            left = mid + 1
        else:
            right = mid
    return min(x - s[left], t[right] - x)

if __name__ == '__main__':
    get_min_distance()
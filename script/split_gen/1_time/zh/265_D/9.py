def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 每个位置的最大值
    max_a = [0] * n
    max_a[0] = a[0]
    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])
    # 每个位置的最小值
    min_a = [0] * n
    min_a[0] = a[0]
    for i in range(1, n):
        min_a[i] = min(min_a[i - 1], a[i])
    # 从右向左遍历，找到满足条件的位置
    w = n - 1
    while w >= 0:
        if max_a[w] == a[w] and min_a[w] == a[w]:
            w -= 1
            continue
        if max_a[w] == a[w]:
            max_a[w] = max_a[w - 1]
            min_a[w] = min(min_a[w - 1], a[w])
            w -= 1
            continue
        if min_a[w] == a[w]:
            min_a[w] = min_a[w - 1]
            max_a[w] = max(max_a[w - 1], a[w])
            w -= 1
            continue
        break
    # 从左向右遍历，找到满足条件的位置
    z = 0
    while z < n:
        if max_a[z] == a[z] and min_a[z] == a[z]:
            z += 1
            continue
        if max_a[z] == a[z]:
            max_a[z] = max_a[z + 1]
            min_a[z] = min(min_a[z + 1], a[z])
            z += 1
            continue
        if min_a[z] == a[z]:
            min_a[z] = min_a[z + 1]
            max_a[z] = max(max_a[z + 1], a[z])
            z += 1
            continue
        break
    # 从左向右遍历，找到满足条件的位置
    y =

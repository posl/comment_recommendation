def is_polygon(n, l):
    if max(l) < sum(l) - max(l):
        return "是"
    else:
        return "否"
n = int(input())
l = list(map(int, input().split()))
print(is_polygon(n, l))

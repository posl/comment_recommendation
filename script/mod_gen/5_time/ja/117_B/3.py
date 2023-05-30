def check_polygon(n, l):
    max = l.pop(l.index(max(l)))
    if max < sum(l):
        return 'Yes'
    else:
        return 'No'
n = int(input())
l = list(map(int, input().split()))
print(check_polygon(n, l))

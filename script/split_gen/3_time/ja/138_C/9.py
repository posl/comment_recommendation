def get_max_value(n, v):
    v.sort()
    result = v[0]
    for i in range(1, n):
        result = (result + v[i]) / 2
    return result
n = int(input())
v = list(map(int, input().split()))
print(get_max_value(n, v))

def get_min_cost():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_cost = float('inf')
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if i == k and j == l:
                        continue
                    cost = a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l))
                    if cost < min_cost:
                        min_cost = cost
    return min_cost

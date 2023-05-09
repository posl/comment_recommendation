def main():
    n, m = map(int, input().split())
    data = []
    for i in range(m):
        p, y = map(int, input().split())
        data.append([p, y, i])
    data.sort(key=lambda x: x[1])
    p = 1
    x = 1
    result = []
    for d in data:
        if p == d[0]:
            result.append([d[2], p, x])
            x += 1
        else:
            p = d[0]
            x = 1
            result.append([d[2], p, x])
            x += 1
    result.sort(key=lambda x: x[0])
    for r in result:
        print(str(r[1]).zfill(6) + str(r[2]).zfill(6))

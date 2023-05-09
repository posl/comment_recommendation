def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    city = [0] * m
    for i in range(m):
        city[i] = [i, p[i], y[i]]
    city.sort(key=lambda x: x[2])
    pre = [0] * (n + 1)
    for i in range(m):
        pre[city[i][1]] += 1
        for j in range(6 - len(str(pre[city[i][1]]))):
            print(0, end='')
        print(pre[city[i][1]], end='')
        for j in range(6 - len(str(city[i][0] + 1))):
            print(0, end='')
        print(city[i][0] + 1)

def main():
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum = 0
            for k in range(d):
                sum += (x[i][k] - x[j][k]) ** 2
            if sum ** 0.5 == int(sum ** 0.5):
                cnt += 1
    print(cnt)

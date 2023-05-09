def distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) ** 2
    return sum ** 0.5
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(x[i], x[j]).is_integer():
            ans += 1
print(ans)

if __name__ == '__main__':
    distance()
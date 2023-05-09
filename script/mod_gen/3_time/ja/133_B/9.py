def calc_distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if calc_distance(x[i], x[j]).is_integer():
            cnt += 1
print(cnt)

if __name__ == '__main__':
    calc_distance()
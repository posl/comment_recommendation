def cal(n, x, y):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            k = (y[i]-y[j])/(x[i]-x[j])
            if k >= -1 and k <= 1:
                cnt += 1
    return cnt
n = int(input())
x = []
y = []
for i in range(n):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)
print(cal(n, x, y))

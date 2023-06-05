def cal(x, X):
    sum = 0
    for i in range(len(X)):
        sum += (X[i] - x) ** 2
    return sum
N = int(input())
X = list(map(int, input().split()))
min = cal(1, X)
for i in range(1, 101):
    if min > cal(i, X):
        min = cal(i, X)
print(min)

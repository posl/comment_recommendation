def cal(x):
    sum = 0
    for i in range(n):
        sum += (x - X[i]) * (x - X[i])
    return sum
n = int(input())
X = list(map(int, input().split()))
X.sort()
print(min(cal(X[n//2]), cal(X[n//2-1])))

def f(x):
    sum = 0
    for i in range(len(X)):
        sum += (X[i] - x)**2
    return sum
N = int(input())
X = list(map(int, input().split()))
X.sort()
print(min([f(i) for i in range(X[0], X[-1]+1)]))

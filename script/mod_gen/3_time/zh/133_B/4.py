def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return d ** 0.5
N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if distance(X[i], X[j]).is_integer():
            count += 1
print(count)

if __name__ == '__main__':
    distance()
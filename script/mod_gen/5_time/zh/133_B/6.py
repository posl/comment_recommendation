def is_integer(num):
    if num == int(num):
        return True
    else:
        return False
N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
count = 0
for i in range(N):
    for j in range(i+1, N):
        distance = 0
        for k in range(D):
            distance += (X[i][k] - X[j][k])**2
        if is_integer(distance**0.5):
            count += 1
print(count)

if __name__ == '__main__':
    is_integer()
def check():
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if ((x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j])):
                    return True
    return False
N = int(input())
x = [0] * N
y = [0] * N
for i in range(0, N):
    x[i], y[i] = map(int, input().split())

if __name__ == '__main__':
    check()
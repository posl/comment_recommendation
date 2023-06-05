def dist(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return d ** 0.5
n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if dist(x[i], x[j]) % 1 == 0:
            cnt += 1
print(cnt)

if __name__ == '__main__':
    dist()
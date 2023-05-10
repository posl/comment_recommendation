def distance(a, b, d):
    total = 0
    for i in range(d):
        total += (a[i] - b[i]) ** 2
    return total ** 0.5
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(x[i], x[j], d).is_integer():
            ans += 1
print(ans)

if __name__ == '__main__':
    distance()
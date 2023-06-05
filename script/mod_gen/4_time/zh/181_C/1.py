def check(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check(points[i], points[j], points[k]):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    check()
def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        x, y = map(int, input().split())
        a[x - 1] += 1
        a[y - 1] += 1
    for i in range(n):
        print(a[i])

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    b = [False] * n
    b[x] = True
    for i in range(n):
        if b[i]:
            b[a[i] - 1] = True
    print(b.count(True))

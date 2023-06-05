def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [False] * n
    b[x - 1] = True
    for i in range(n):
        if b[i]:
            a[i] -= 1
            b[a[i]] = True
    print(b.count(True))

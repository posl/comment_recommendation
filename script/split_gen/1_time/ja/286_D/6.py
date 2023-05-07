def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(2 ** n):
        y = 0
        for j in range(n):
            if (i >> j) & 1:
                y += a[j] * b[j]
        if y == x:
            print("Yes")
            return
    print("No")

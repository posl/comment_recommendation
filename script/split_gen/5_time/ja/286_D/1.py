def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        at, bt = map(int, input().split())
        a.append(at)
        b.append(bt)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

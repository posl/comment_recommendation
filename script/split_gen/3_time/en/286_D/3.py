def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(n):
        if x - a[i] * b[i] >= 0:
            x -= a[i] * b[i]
        else:
            x -= (x // a[i]) * a[i]
    if x == 0:
        print("Yes")
    else:
        print("No")
main()

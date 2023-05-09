def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            sum += a[i] - 1
        else:
            sum += a[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

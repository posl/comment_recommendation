def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += a[i]
        else:
            total += a[i] - 1
    if total <= x:
        print("Yes")
    else:
        print("No")

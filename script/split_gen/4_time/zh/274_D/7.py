def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if a[-1] > abs(x) or a[-1] > abs(y):
        print("No")
        return
    if (abs(x) + abs(y)) % 2 != a[-1] % 2:
        print("No")
        return
    print("Yes")

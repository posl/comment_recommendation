def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(abs(x-y))
    a.sort(reverse=True)
    for i in range(n):
        for j in range(i+1, n+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    i = 0
    while i < n:
        if x < y:
            x, y = y, x
        if x == a[i] and y == a[i+1]:
            x -= a[i]
            y -= a[i+1]
            i += 2
        elif x == a[i]:
            x -= a[i]
            i += 1
        elif y == a[i]:
            y -= a[i]
            i += 1
        else:
            print("No")
            return
    if x == 0 and y == 0:
        print("Yes")
    else:
        print("No")

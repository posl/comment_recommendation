def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n):
        if a[i] == a[i+1]:
            print("No")
            exit()
    if x - a[-1] < 0 or y - a[-1] < 0:
        print("No")
        exit()
    if x - a[-1] == 0 and y - a[-1] == 0:
        print("Yes")
        exit()
    if x - a[-1] == 0:
        print("No")
        exit()
    if y - a[-1] == 0:
        print("No")
        exit()
    print("Yes")

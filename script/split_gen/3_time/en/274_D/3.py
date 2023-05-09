def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] - a[j])**2 + (i - j)**2 == (a[i] - a[j])**2:
                print("Yes")
                exit()
    print("No")

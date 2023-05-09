def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x: x[1])
    for i in range(n):
        if a[i][0] <= x <= a[i][1]:
            print("Yes")
            return
    print("No")

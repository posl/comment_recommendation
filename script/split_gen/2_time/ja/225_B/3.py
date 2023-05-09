def main():
    n = int(input())
    a = [0] * (n + 1)
    for i in range(n - 1):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    for i in range(n + 1):
        if a[i] == n - 1:
            print("Yes")
            return
    print("No")

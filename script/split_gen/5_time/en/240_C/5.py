def main():
    n, x = map(int, input().split())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    if a[0] > x or b[0] < x:
        print("No")
        return
    for i in range(1, n):
        if a[i] > b[i-1]:
            print("No")
            return
    print("Yes")

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    distance = 0
    for i in range(n):
        distance += a[i]
        if distance > x:
            print("No")
            exit()
        distance += b[i]
    if distance > x:
        print("No")
    else:
        print("Yes")

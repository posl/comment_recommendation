def main():
    n, m, t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    bat = n
    prev = 0
    for i in range(m):
        bat -= a[i] - prev
        if bat <= 0:
            print("No")
            exit()
        bat += b[i] - a[i]
        bat = min(bat, n)
        prev = b[i]
    bat -= t - prev
    if bat <= 0:
        print("No")
    else:
        print("Yes")

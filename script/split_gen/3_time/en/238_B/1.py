def main():
    n = int(input())
    a = list(map(int, input().split()))
    angle = 0
    for i in range(n):
        angle += a[i]
        angle %= 360
    print((360 - angle) % 360)

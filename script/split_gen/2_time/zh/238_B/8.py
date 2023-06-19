def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_angle = 0
    for i in range(n):
        angle = 0
        for j in range(n):
            angle += a[(i + j) % n]
            if angle > 180:
                angle = 360 - angle
            max_angle = max(max_angle, angle)
    print(360 - max_angle)

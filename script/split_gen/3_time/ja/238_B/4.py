def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    max_angle = 0
    for i in range(n):
        angle = abs(a[i] - a[i+1])
        if angle > 180:
            angle = 360 - angle
        max_angle = max(max_angle, angle)
    print(360-max_angle)

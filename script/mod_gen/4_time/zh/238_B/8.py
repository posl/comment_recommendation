def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(360 - a[0])
    else:
        max_angle = 0
        for i in range(n):
            for j in range(i, n):
                angle = a[j] - a[i]
                if angle < 0:
                    angle += 360
                max_angle = max(max_angle, angle)
        print(360 - max_angle)

if __name__ == '__main__':
    main()
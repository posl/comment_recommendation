def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    max_angle = 0
    for i in range(n):
        max_angle = max(max_angle, a[i+2]-a[i])
    print(360-max_angle)

if __name__ == '__main__':
    main()
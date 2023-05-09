def main():
    n = int(input())
    a = list(map(int, input().split()))
    angles = [0]
    for i in range(n):
        angles.append(angles[-1] + a[i])
    angles = [angle % 360 for angle in angles]
    angles.sort()
    ans = 360
    for i in range(n):
        ans = min(ans, angles[i + 1] - angles[i])
    print(ans)

if __name__ == '__main__':
    main()
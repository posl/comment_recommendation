def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append([x, y, r])
    print(solve(circles, sx, sy, tx, ty))

if __name__ == '__main__':
    main()
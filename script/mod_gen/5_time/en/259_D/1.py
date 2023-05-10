def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    print('Yes' if solve(sx, sy, tx, ty, circles) else 'No')

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [tuple(map(int, input().split())) for _ in range(n)]
    xyr.append((sx, sy, 0))
    xyr.append((tx, ty, 0))
    print('Yes' if solve(n, xyr) else 'No')

if __name__ == '__main__':
    main()
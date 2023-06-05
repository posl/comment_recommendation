def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    if ax * by + bx * cy + cx * dy + dx * ay - ay * bx - by * cx - cy * dx - dy * ax > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
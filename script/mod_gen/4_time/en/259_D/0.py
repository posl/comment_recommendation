def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    # Check if the start and goal are on the circumference of at least one of the circles
    for x, y, r in circles:
        if (x - sx) ** 2 + (y - sy) ** 2 == r ** 2 and (x - tx) ** 2 + (y - ty) ** 2 == r ** 2:
            print("Yes")
            return
    # Check if the goal is reachable from the start
    for x1, y1, r1 in circles:
        if (x1 - sx) ** 2 + (y1 - sy) ** 2 > r1 ** 2:
            continue
        for x2, y2, r2 in circles:
            if (x2 - tx) ** 2 + (y2 - ty) ** 2 > r2 ** 2:
                continue
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()
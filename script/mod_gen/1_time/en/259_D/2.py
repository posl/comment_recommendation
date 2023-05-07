def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    ans = "No"
    for x, y, r in circles:
        if ((sx - x) ** 2 + (sy - y) ** 2) ** 0.5 < r and ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5 < r:
            continue
        if ((sx - x) ** 2 + (sy - y) ** 2) ** 0.5 < r or ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5 < r:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()
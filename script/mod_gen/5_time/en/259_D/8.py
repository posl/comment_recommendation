def solve():
    #print("solve")
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    #print(n, sx, sy, tx, ty)
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    #print(circles)
    #print("solve")
    return "Yes"
print(solve())

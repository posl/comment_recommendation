def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    x = []
    y = []
    r = []
    for i in range(N):
        x_, y_, r_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        r.append(r_)
    print("Yes" if solve(sx, sy, tx, ty, x, y, r) else "No")

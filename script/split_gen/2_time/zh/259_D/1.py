def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    print('Yes')

def main():
    W, H, x, y = map(int, input().split())
    ans = 0
    if x == W/2 and y == H/2:
        ans = 1
    print(W*H/2, ans)

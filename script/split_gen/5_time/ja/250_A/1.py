def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    if R == 1 or R == H:
        ans += 1
    if C == 1 or C == W:
        ans += 1
    print(ans)

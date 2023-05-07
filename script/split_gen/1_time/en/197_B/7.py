def main():
    # Read input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    # Count visible squares
    ans = 1
    for i in range(X - 1, 0, -1):
        if S[i - 1][Y - 1] == ".":
            ans += 1
        else:
            break
    for i in range(X + 1, H + 1):
        if S[i - 1][Y - 1] == ".":
            ans += 1
        else:
            break
    for j in range(Y - 1, 0, -1):
        if S[X - 1][j - 1] == ".":
            ans += 1
        else:
            break
    for j in range(Y + 1, W + 1):
        if S[X - 1][j - 1] == ".":
            ans += 1
        else:
            break
    # Output
    print(ans)

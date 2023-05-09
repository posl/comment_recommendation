def main():
    X, Y, N = map(int, input().split())
    ans = 0
    if N % 3 == 0:
        ans = N // 3 * Y
    else:
        ans = N // 3 * Y + (N % 3) * X
    print(ans)

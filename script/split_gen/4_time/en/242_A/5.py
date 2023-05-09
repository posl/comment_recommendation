def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        ans = 1
    elif A < X <= B:
        ans = 1 - ((B - X + 1) / (B - A + 1)) * (C / (B - A + 1))
    else:
        ans = 0
    print(ans)

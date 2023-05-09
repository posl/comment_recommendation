def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y and X * A - X <= B:
        X *= A
        ans += 1
    ans += (Y - 1 - X) // B
    print(ans)

def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            ans += 1
        else:
            break
    ans += (Y - X - 1) // B
    print(ans)

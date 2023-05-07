def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while True:
        if X * A < X + B:
            if X * A < Y:
                X *= A
                ans += 1
            else:
                break
        else:
            ans += (Y - X - 1) // B
            break
    print(ans)

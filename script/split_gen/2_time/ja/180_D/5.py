def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while True:
        if X * A >= Y:
            break
        if X * A - X <= B:
            break
        X *= A
        ans += 1
    ans += (Y - X - 1) // B
    print(ans)

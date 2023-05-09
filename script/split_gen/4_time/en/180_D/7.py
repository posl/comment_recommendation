def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while A*X < Y and A*X < X+B:
        X *= A
        ans += 1
    ans += (Y-X-1)//B
    print(ans)

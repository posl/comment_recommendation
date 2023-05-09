def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X*(A-1) < B and X*A < Y:
        X *= A
        ans += 1
    ans += (Y-1-X)//B
    print(ans)

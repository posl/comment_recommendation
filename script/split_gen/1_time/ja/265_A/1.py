def main():
    X, Y, N = map(int, input().split())
    ans = 0
    while N > 0:
        if N >= 3:
            N -= 3
            ans += Y
        else:
            N -= 1
            ans += X
    print(ans)

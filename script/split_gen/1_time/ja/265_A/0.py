def main():
    X, Y, N = map(int, input().split())
    ans = 0
    while N > 0:
        if N >= 3:
            ans += Y
            N -= 3
        else:
            ans += X
            N -= 1
    print(ans)

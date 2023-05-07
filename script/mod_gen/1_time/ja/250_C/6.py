def main():
    N, Q = map(int, input().split())
    ball = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        p = ball.index(x)
        if p == N-1:
            ball[p], ball[p-1] = ball[p-1], ball[p]
        else:
            ball[p], ball[p+1] = ball[p+1], ball[p]
    print(*ball)

if __name__ == '__main__':
    main()
def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        ball[x - 1], ball[x] = ball[x], ball[x - 1]
    print(*ball)

if __name__ == '__main__':
    main()
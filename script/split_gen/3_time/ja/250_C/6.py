def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        if x == N:
            ball[x-1], ball[0] = ball[0], ball[x-1]
        else:
            ball[x-1], ball[x] = ball[x], ball[x-1]
    print(*ball)

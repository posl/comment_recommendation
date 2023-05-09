def main():
    n, q = map(int, input().split())
    ball = [0] * n
    for i in range(n):
        ball[i] = i + 1
    for i in range(q):
        x = int(input())
        for j in range(n):
            if ball[j] == x:
                ball[j], ball[j + 1] = ball[j + 1], ball[j]
                break
    for i in range(n):
        print(ball[i], end=" ")

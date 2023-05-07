def main():
    N = int(input())
    a = list(map(int, input().split()))
    ball = []
    for i in range(N):
        ball.append(a[i])
        if len(ball) >= 2:
            if ball[-1] == ball[-2]:
                ball.pop()
                ball.pop()
    print(N - len(ball))

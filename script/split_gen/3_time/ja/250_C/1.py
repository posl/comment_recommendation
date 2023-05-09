def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input())
        balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

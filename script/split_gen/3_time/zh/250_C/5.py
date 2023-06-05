def swap(i, balls):
    if i == len(balls) - 1:
        balls[i], balls[0] = balls[0], balls[i]
    else:
        balls[i], balls[i+1] = balls[i+1], balls[i]
    return balls
N, Q = list(map(int, input().split()))
balls = list(range(1, N+1))
for _ in range(Q):
    x = int(input())
    balls = swap(x-1, balls)
print(' '.join(map(str, balls)))

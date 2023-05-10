def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
N, Q = map(int, input().split())
balls = [i for i in range(1, N + 1)]
for _ in range(Q):
    x = int(input())
    if balls[x - 1] == x:
        continue
    if x == 1 or balls[x - 2] != x:
        balls[x - 1], balls[x] = swap(balls[x - 1], balls[x])
    else:
        balls[x - 2], balls[x - 1] = swap(balls[x - 2], balls[x - 1])
print(*balls)

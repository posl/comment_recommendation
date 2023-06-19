def swap(a, b):
    return b, a
N, Q = map(int, input().split())
balls = [i for i in range(1, N+1)]
for i in range(Q):
    x = int(input())
    balls[x-1], balls[x] = swap(balls[x-1], balls[x])
print(' '.join(map(str, balls)))

if __name__ == '__main__':
    swap()
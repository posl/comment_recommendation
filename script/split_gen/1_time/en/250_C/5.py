def main():
    #input
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    #compute
    balls = [i for i in range(1, N+1)]
    for x in X:
        i = balls.index(x)
        if i == N-1:
            balls[i], balls[i-1] = balls[i-1], balls[i]
        else:
            balls[i], balls[i+1] = balls[i+1], balls[i]
    #output
    print(*balls)

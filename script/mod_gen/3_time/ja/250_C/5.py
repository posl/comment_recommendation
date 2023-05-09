def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        if x == 1:
            balls[0], balls[1] = balls[1], balls[0]
        elif x == N:
            balls[N-2], balls[N-1] = balls[N-1], balls[N-2]
        else:
            balls[x-2], balls[x-1] = balls[x-1], balls[x-2]
    print(*balls)

if __name__ == '__main__':
    main()
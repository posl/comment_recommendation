def main():
    N, Q = map(int, input().split())
    balls = list(range(N+1))
    for i in range(Q):
        x = int(input())
        balls[x], balls[x+1] = balls[x+1], balls[x]
    print(*balls[1:])

if __name__ == '__main__':
    main()
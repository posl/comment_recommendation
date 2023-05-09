def main():
    n, q = map(int, input().split())
    balls = list(range(1, n+1))
    for i in range(q):
        x = int(input())
        balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

if __name__ == '__main__':
    main()
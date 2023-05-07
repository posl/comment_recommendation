def main():
    N, M = map(int, input().split())
    balls = [0] * (N+1)
    for i in range(M):
        k = int(input())
        for ball in map(int, input().split()):
            balls[ball] += 1
    print('Yes' if all(ball % 2 == 0 for ball in balls) else 'No')

if __name__ == '__main__':
    main()
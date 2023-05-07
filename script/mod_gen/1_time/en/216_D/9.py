def main():
    N, M = map(int, input().split())
    # 1-indexed
    ball_count = [0] * (N + 1)
    for _ in range(M):
        k = int(input())
        balls = list(map(int, input().split()))
        for ball in balls:
            ball_count[ball] += 1
    for count in ball_count:
        if count % 2 == 1:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
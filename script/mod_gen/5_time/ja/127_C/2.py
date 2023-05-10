def main():
    N, M = map(int, input().split())
    min_left = 0
    max_right = N + 1
    for i in range(M):
        left, right = map(int, input().split())
        min_left = max(min_left, left)
        max_right = min(max_right, right)
    print(max(max_right - min_left + 1, 0))

if __name__ == '__main__':
    main()
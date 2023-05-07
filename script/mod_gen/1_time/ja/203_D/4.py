def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
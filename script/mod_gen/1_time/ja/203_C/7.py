def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    cnt = 0
    for a, b in AB:
        cnt += b
        if cnt >= K:
            print(a)
            break

if __name__ == '__main__':
    main()
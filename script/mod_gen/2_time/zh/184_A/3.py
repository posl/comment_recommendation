def main():
    N, W = map(int, input().split())
    stp = [list(map(int, input().split())) for _ in range(N)]
    stp.sort(key=lambda x: x[0])
    cnt = 0
    for s, t, p in stp:
        cnt += p
        if cnt > W:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
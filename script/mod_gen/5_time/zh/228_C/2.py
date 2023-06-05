def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()